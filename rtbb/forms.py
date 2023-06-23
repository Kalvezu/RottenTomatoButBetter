from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField, EmailField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    loginSubmit = SubmitField('Login')

class registerForm(FlaskForm):
    email = EmailField('E-Mail', validators=[DataRequired()], render_kw={"placeholder": "E-Mail"})
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired()], render_kw={"placeholder": "Confirm Password"})
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