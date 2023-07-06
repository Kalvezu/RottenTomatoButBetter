from rtbb import app, db, get_locale
from flask import render_template, flash, redirect, url_for, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from rtbb.forms import LoginForm, movieForm, deleteMovie, updateForm, registerForm, forgotPasswordForm
from flask_login import login_user, LoginManager, login_required, logout_user
from rtbb.models import Login, Movies
from flask_babel import gettext
import os
import random

#---------------------------------------------------------------------------------------------------------------------------------------------------------------<>
#Config für Login/Register/Forgot Password/Auth
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

image_folder = "rtbb/static/covers"

@login_manager.user_loader
def load_user(id):
    return Login.query.get(int(id))

@app.context_processor
def inject_dark_mode():
    def get_dark_mode():
        return session.get('dark_mode', False)
    return {'dark_mode': get_dark_mode()}

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = Login.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash(gettext('Failed to login'), 'danger')

    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    register = registerForm()
    login = Login.query.all()

    if register.validate_on_submit():
        login = Login(
            username=register.username.data,
            password=generate_password_hash(register.password.data),
            email=register.email.data,
        )
        db.session.add(login)
        db.session.commit()

        flash(gettext('User created successfully!'), 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=register)

@app.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPassword():
    form = forgotPasswordForm()

    if form.validate_on_submit():
        email = form.email.data
        new_password = form.password.data
        confirm_password = form.confirmPassword.data

        user = Login.query.filter_by(email=email).first()

        if user and new_password == confirm_password: 
            user.password = generate_password_hash(form.password.data)
            db.session.commit()

            return redirect(url_for('login'))
        else:
            flash(gettext('Failed to update password'), 'danger')        

    return render_template('forgotPassword.html', form=form)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------<>
#Game
@app.route('/compare_images', methods=['POST'])
def compare_images():    
    choice = request.form.get('choice')
    current_right_image = request.args.get('current_right_image')
    current_left_image = request.args.get('current_left_image')
    image_files = os.listdir(image_folder)

    right_image = Movies.query.filter_by(photoname = current_right_image).first_or_404()
    left_image = Movies.query.filter_by(photoname = current_left_image).first_or_404()

    durationOne = right_image.duration
    durationTwo = left_image.duration    

    counter = 0
    if choice == 'higher':
        if(durationOne <= durationTwo):
            counter += 1
            image_files.remove(current_left_image)
            current_left_image = current_right_image
            current_right_image = random.choice(image_files)
        else:
          return render_template('verloren.html')
    elif choice == 'lower':
        if(durationOne >= durationTwo):
            counter += 1
            image_files.remove(current_left_image)
            current_left_image = current_right_image
            current_right_image = random.choice(image_files)
        else:
            return render_template('verloren.html')

    return render_template('releasedate.html', current_right_image=current_right_image, current_left_image=current_left_image)

@app.route('/releasedate')
def releasedate():
    
    image_files = os.listdir(image_folder)
    
    if image_files:
        current_right_image = random.choice(image_files)
        current_left_image = random.choice(image_files)
        image_files.remove(current_left_image)
    else:
        current_right_image = None
        current_left_image = None


    return render_template('releasedate.html', current_right_image=current_right_image, current_left_image=current_left_image)

@app.route('/runtime')
def runtime():
    mov = Movies.query.all()
    
    return render_template('runtime.html', mov=mov)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------<>
#Sonstigens
@app.route('/') 
@login_required
def home():
    
    current_language = get_locale()
    languages = app.config['LANGUAGES']
    return render_template('home.html', languages=languages, current_language=current_language)

@app.route('/quellen')
@login_required
def quellen():
    return render_template('quellen.html')

@app.route('/verloren')
@login_required
def verloren():
    return render_template('verloren.html')

@app.route('/impressum')
@login_required
def impressum():
    return render_template('impressum.html')

@app.route('/discord')
def discord():
    return render_template('socialmedias/discord.html')

@app.route('/twitter')
def twitter():
    return render_template('socialmedias/twitter.html')

@app.route('/facebook')
def facebook():
    return render_template('socialmedias/facebook.html')

@app.route('/linkedin')
def linkedin():
    return render_template('socialmedias/linkedin.html')

@app.route('/youtube')
def youtube():
    return render_template('socialmedias/youtube.html')

@app.route('/instagram')
def instagram():
    return render_template('socialmedias/instagram.html')

@app.route('/toggle_dark_mode')
def toggle_dark_mode():
    if 'dark_mode' in session:
        session.pop('dark_mode')
    else:
        session['dark_mode'] = True
    return redirect(request.referrer or url_for('home'))

@app.route('/set_language/<lang_code>')
def set_language(lang_code):
    session['language'] = lang_code
    return redirect(request.referrer or url_for('home'))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------<>
# Config for CRUD
@app.route('/update/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def update(movie_id):
    movie = Movies.query.get_or_404(movie_id)
    update_form = updateForm(obj=movie)

    if update_form.validate_on_submit():
        movie.title = update_form.title.data
        movie.director = update_form.director.data
        movie.duration = update_form.duration.data
        movie.description = update_form.description.data
        db.session.commit()

        flash(gettext('Movie updated successfully!'), 'success')
        return redirect(url_for('crud'))
    
    return render_template('update.html', update_form=update_form, movie=movie)

@app.route('/crud', methods=['GET', 'POST'])
@login_required
def crud():
    addMovies = movieForm()
    delete = deleteMovie()
    movies = Movies.query.all()

    if addMovies.validate_on_submit():
        movie = Movies(
            title=addMovies.title.data,
            director=addMovies.director.data,
            duration=addMovies.duration.data,
            description=addMovies.description.data
        )
        db.session.add(movie)
        db.session.commit()

        flash(gettext('Movie added successfully!'), 'success')
        return redirect(url_for('home'))

    if delete.validate_on_submit():
        movie_id = request.form['movie_id']
        return redirect(url_for('delete_movie', movie_id=movie_id))
    
    return render_template('crud.html', addMovies=addMovies, delete=delete, movies=movies)

@app.route('/delete/<int:movie_id>', methods=['POST'])
@login_required
def delete_movie(movie_id):
    delete = deleteMovie()

    if delete.validate_on_submit():
        movie = Movies.query.get_or_404(movie_id)
        db.session.delete(movie)
        db.session.commit()
        flash(gettext('Movie deleted successfully!'), 'success')
        return redirect(url_for('crud'))