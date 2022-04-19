from email import message
import os
from telnetlib import GA
from main import app,secure_filename,db
from flask import redirect,render_template,request,url_for,session,flash
from main.models import SlideShow, ClubDocument,About,Question,Gallery,News,Contact,ContactUs

@app.route('/', methods=['GET', 'POST'])
def index():
    gallery = Gallery.query.all()
    ssphotos = SlideShow.query.all();
    about = About.query.get(1);
    question = Question.query.get(1);
    news = News.query.get(1)

    if request.method == 'POST':
        content_to_create = ContactUs(name = request.form.get('name'),
                                      lastname = request.form.get('lastname'),
                                      email = request.form.get('email'),
                                      number = request.form.get('phone'),
                                      message = request.form.get('message')  )
        db.session.add(content_to_create)
        db.session.commit()
        return redirect(url_for('index'))    
    return render_template('index.html', ssphotos=ssphotos,gallery=gallery,about=about,question=question,news=news)

@app.route('/admin')
def admin():
    return render_template('admin/index.html')

#--------------------------Admin/SlideShow--------------------------

@app.route('/admin/SlideShowAdd', methods=["GET","POST"])
def SlideShowAdd():
    if request.method == "POST":
        f = request.files['photo']
        fname = f.filename
        if fname:
            f.save(os.path.join('main\static\img\slideshow', secure_filename(fname)))
        content_to_create = SlideShow(title = request.form.get('title'),
                                      file = fname)
        db.session.add(content_to_create)
        db.session.commit()
        flash('Content Added')
        return redirect(url_for('SlideShowInfo'))
    return render_template('admin/SlideShow/SlideShowAdd.html')

@app.route('/admin/SlideShowUpdate/<int:id>', methods=["GET","POST"])
def SlideShowUpdate(id):
    model = SlideShow.query.get(id)
    if request.method == 'POST':
        f = request.files['photo']
        fname = f.filename
        if fname:
            os.remove(os.path.join('main\static\img\slideshow', model.file))
            f.save(os.path.join('main\static\img\slideshow', secure_filename(fname)))
            model.file = fname
            #Kohne sekili sil
        model.title = request.form.get('title')
        db.session.commit()
        flash('Content Updated')
        return redirect(url_for('SlideShowInfo'))
    return render_template('admin/SlideShow/SlideShowUpdate.html', content=model)

@app.route('/admin/SlideShow', methods=['GET'])
def SlideShowInfo():
    model = SlideShow.query.all()
    return render_template('admin/SlideShow/SlideShowInfo.html', content=model) 

@app.route('/admin/SlideShowDelete/<int:id>')
def SlideShowDelete(id):
    model = SlideShow.query.get(id)
    file_path = os.path.join('main/static/img/slideshow',model.file)
    if model.file:
        if file_path:
            os.remove(file_path)
    db.session.delete(model)
    db.session.commit()
    flash('Content Deleted')
    return redirect(url_for('SlideShowInfo'))


@app.route('/admin/ClubDocument', methods=['GET','POST'])
def ClubDocumentInfo():
    model = ClubDocument.query.all()
    return render_template('admin/ClubDocument/ClubDocument.html', content=model)

@app.route('/admin/ClubDocumentUpdate')
def ClubDocumentUpdate():
    model = ClubDocument.query.get(1)
    if request.method == "POST":
        f =  request.files['document']
        fname = f.filename
        if fname:
            os.remove(os.path.join('main/satatic/ClubDocument', model.file))
            f.save(os.path.join('main/static/ClubDocument',fname))
            model.file = fname
        model.text = request.form.get['text']
        db.session.commit()
        flash('Content Updated')
        return redirect(url_for('ClubDocument'))
    return render_template('admin/ClubDocument/ClubDocumentUpdate.html', content=model)

@app.route('/admin/about', methods=['GET','POST'])
def about():
    model = About.query.get(1)
    if request.method == 'POST':
        f = request.files['file']
        fname = f.filename
        if fname:
            f.save(os.path.join('main/static/img/about', secure_filename(fname)))
            model.photo = fname
        model.text = request.form.get('about')
        db.session.commit()
        return redirect(url_for('about'))
    return render_template('admin/About/about.html', content=model)

@app.route('/admin/question', methods=['GET','POST'])
def question():
    model = Question.query.get(1)
    if request.method == 'POST':
        model.text = request.form.get('text')
        db.session.commit()
        return redirect(url_for('question'))
    return render_template('admin/Question/question.html', content=model)

@app.route('/admin/gallery', methods=['GET','POST'])
def gallery():
    model = Gallery.query.all()
    if request.method == 'POST':
        f = request.files['file']
        fname = f.filename
        if fname:
            f.save(os.path.join('main/static/img/gallery', secure_filename(fname)))
            content_to_create = Gallery(file=fname)
            db.session.add(content_to_create)
            db.session.commit()
            flash('Img Saved')
            return redirect(url_for('gallery'))
    return render_template('admin/Gallery/gallery.html', content = model)

@app.route('/admin/gallery/<int:id>', methods=['GET','POST'])
def galleryDelete(id):
    model = Gallery.query.get(id)
    file_path=os.path.join('main/static/img/gallery', model.file)
    os.remove(file_path)
    db.session.delete(model)
    db.session.commit()
    flash('img deleted')
    return redirect(url_for('gallery'))

@app.route('/admin/news', methods=['GET','POST'])
def news():
    model = News.query.get(1)
    if request.method == 'POST':
        model.text = request.form.get('news')
        db.session.commit()
        flash('Upgrade Success')
        return redirect(url_for('news'))
    return render_template('admin/News/news.html', content=model)

@app.route('/admin/contacUs',methods=['GET', 'POST'])
def contactUs():
    model = ContactUs.query.all()
    return render_template('admin/ContactUs/contactUs.html', content=model)

@app.route('/admin/contactUs/<int:id>', methods=['GET','POST'])
def contactUsDelete(id):
    model = ContactUs.query.get(id)
    db.session.delete(model)
    db.session.commit()
    return redirect(url_for('contactUs'))