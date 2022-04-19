from main import db
from sqlalchemy import Integer,String

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
    message = db.Column(db.String())

class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    number = db.Column(db.String())
    email = db.Column(db.String())