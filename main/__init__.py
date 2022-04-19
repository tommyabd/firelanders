from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_ckeditor import CKEditor
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'main/static/img'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firelanders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '5209a08cfb7acebb31ae9915'   
db = SQLAlchemy(app)
migrate = Migrate(app,db)
csrf = CSRFProtect(app)
ckeditor = CKEditor(app)

from main import routes