from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@109.123.252.51/postgres'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

from rtbb import routes