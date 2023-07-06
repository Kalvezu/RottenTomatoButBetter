from flask_babel import gettext, lazy_gettext
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Length, ValidationError
from rtbb.models import Login

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": lazy_gettext("Username")})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": lazy_gettext("Password")})
    loginSubmit = SubmitField('Login')
    
class RegisterForm(FlaskForm):
    email = EmailField('E-Mail', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired()])
    registerSubmit = SubmitField('Register')

class registerForm(FlaskForm):
    email = EmailField('E-Mail', validators=[DataRequired()], render_kw={"placeholder": lazy_gettext("E-Mail")})
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)], render_kw={"placeholder": lazy_gettext("Username")})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)], render_kw={"placeholder": lazy_gettext("Password")})
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired()], render_kw={"placeholder": lazy_gettext("Confirm Password")})
    loginSubmit = SubmitField(lazy_gettext('register'))

    def validate_creation(self, username, email):
        existing_user = Login.query.filter_by(username.data).first()
        existing_email = Login.query.filter_by(email.data).first()

        if existing_user or existing_email:
            raise ValidationError(lazy_gettext("Username or E-Mail already exists. Please choose a different one"))

class forgotPasswordForm(FlaskForm):
    email = EmailField('E-Mail', validators=[DataRequired()], render_kw={"placeholder": lazy_gettext("E-Mail")})
    password = PasswordField('New password', validators=[DataRequired()], render_kw={"placeholder": lazy_gettext("New password")})
    confirmPassword = PasswordField('Confirm new password', validators=[DataRequired()], render_kw={"placeholder": lazy_gettext("Confirm new password")})
    confirmSubmit = SubmitField(lazy_gettext('Confirm'))

class movieForm(FlaskForm):
    title = StringField(lazy_gettext('Title'), validators=[DataRequired()])
    director = StringField(lazy_gettext('Director'), validators=[DataRequired()])
    duration = IntegerField(lazy_gettext('Duration'), validators=[DataRequired()])
    description = TextAreaField(lazy_gettext('Description'), validators=[DataRequired()])
    movieSubmit = SubmitField(lazy_gettext('Submit'))

class updateForm(FlaskForm):
    title = StringField(lazy_gettext('Title:'), validators=[DataRequired()])
    director = StringField(lazy_gettext('Director:'), validators=[DataRequired()])
    duration = IntegerField(lazy_gettext('Duration(in Minutes):'), validators=[DataRequired()])
    description = TextAreaField(lazy_gettext('Description:'), validators=[DataRequired()])
    updateSubmit = SubmitField(lazy_gettext('Edit'))

class deleteMovie(FlaskForm):
    deleteSubmit = SubmitField(lazy_gettext('Delete'))