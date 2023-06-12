from rtbb import db
from datetime import datetime

class Login(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    director = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    added_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)