from main import db,bcrypt,loginmanager
from sqlalchemy import Integer,String
from flask_login import UserMixin

@loginmanager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password_hash = db.Column(db.String())

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

class SlideShow(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    file = db.Column(db.String(), nullable=False) 

class ClubDocument(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String())
    file = db.Column(db.String())

class About(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    text = db.Column(db.String())
    photo = db.Column(db.String())

class Question(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String())

class Gallery(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    file = db.Column(db.String())

class News(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String())

class CounterDown(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    day = db.Column(db.Integer())
    hours = db.Column(db.Integer())
    minutes = db.Column(db.Integer())
    seconds = db.Column(db.Integer())

class VideoLink(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    link = db.Column(db.String())

class ContactUs(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    lastname = db.Column(db.String())
    email = db.Column(db.String())
    number = db.Column(db.String())
    bikeModel = db.Column(db.String())
    message = db.Column(db.String())

class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    number = db.Column(db.String())
    email = db.Column(db.String())

class CountDown(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.String())
    time = db.Column(db.String())

class YoutubeVideo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.String())