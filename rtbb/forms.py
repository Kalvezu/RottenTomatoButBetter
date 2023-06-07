from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    loginSubmit = SubmitField('Login')

class movieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    director = StringField('Director', validators=[DataRequired()])
    duration = IntegerField('Duration', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    movieSubmit = SubmitField('Submit')

class updateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    director = StringField('Director', validators=[DataRequired()])
    duration = IntegerField('Duration', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    updateSubmit = SubmitField('Edit')

class deleteMovie(FlaskForm):
    deleteSubmit = SubmitField('Delete')