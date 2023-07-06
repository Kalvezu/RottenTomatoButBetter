from rtbb import db
from datetime import datetime
from flask_login import UserMixin

class Login(db.Model, UserMixin):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(320), nullable=False)
    email = db.Column(db.String(320), nullable=False, unique=True)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    director = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    realeasedate = db.Column(db.DateTime, nullable=False)
    photoname = db.Column(db.String(50), nullable=False)
    added_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)