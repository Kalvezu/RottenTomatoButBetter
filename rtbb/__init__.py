from flask import Flask, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel, get_locale, _
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@109.123.252.51/postgres'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
app.config['WTF_I18N_ENABLED'] = True
app.config['BABEL_DEFAULT_LOCALE'] = 'de'
app.config['LANGUAGES'] = {'en': 'English', 'de': 'Deutsch', 'pt': 'Português'}

db = SQLAlchemy(app)
babel = Babel(app)

def get_locale():
    language = session.get('language')

    if not language:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    
    return language

babel.init_app(app, locale_selector=get_locale)

@app.context_processor
def inject_languages():
    return dict(languages=app.config['LANGUAGES'])

@app.context_processor
def inject_current_language():
    return dict(current_language=get_locale())

with app.app_context():
    db.create_all()

from rtbb import routes