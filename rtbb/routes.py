from rtbb import app, db
from flask import render_template, flash, redirect, url_for, request
from rtbb.forms import LoginForm, movieForm, deleteMovie, updateForm
from rtbb.models import Login, Movies

@app.route('/') 
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
    
        user = Login.query.filter_by(username=username).first()
        
        if user and user.password == password:
            return redirect(url_for('home'))
        else:
            flash('Failed to login', 'danger')

    return render_template('login.html', form=form)

@app.route('/quellen')
def quellen():
    return render_template('quellen.html')

@app.route('/impressum')
def impressum():
    return render_template('impressum.html')

@app.route('/runtime')
def runtime():
    return render_template('runtime.html')

@app.route('/releasedate')
def releasedate():
    return render_template('releasedate.html')



@app.route('/discord')
def discord():
    return render_template('fakes/discord.html')

@app.route('/twitter')
def twitter():
    return render_template('fakes/twitter.html')

@app.route('/facebook')
def facebook():
    return render_template('fakes/facebook.html')

@app.route('/linkedin')
def linkedin():
    return render_template('fakes/linkedin.html')

@app.route('/youtube')
def youtube():
    return render_template('fakes/youtube.html')

@app.route('/instagram')
def instagram():
    return render_template('fakes/instagram.html')


# Config for CRUD
@app.route('/update/<int:movie_id>', methods=['GET', 'POST'])
def update(movie_id):
    movie = Movies.query.get_or_404(movie_id)
    update_form = updateForm(obj=movie)

    if update_form.validate_on_submit():
        movie.title = update_form.title.data
        movie.director = update_form.director.data
        movie.duration = update_form.duration.data
        movie.description = update_form.description.data
        db.session.commit()

        flash('Movie updated successfully!', 'success')
        return redirect(url_for('crud'))
    
    return render_template('update.html', update_form=update_form, movie=movie)

@app.route('/crud', methods=['GET', 'POST'])
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

        flash('Movie added successfully!', 'success')
        return redirect(url_for('home'))

    if delete.validate_on_submit():
        movie_id = request.form['movie_id']
        return redirect(url_for('delete_movie', movie_id=movie_id))
    
    return render_template('crud.html', addMovies=addMovies, delete=delete, movies=movies)

@app.route('/delete/<int:movie_id>', methods=['POST'])
def delete_movie(movie_id):
    delete = deleteMovie()

    if delete.validate_on_submit():
        movie = Movies.query.get_or_404(movie_id)
        db.session.delete(movie)
        db.session.commit()
        flash('Movie deleted successfully!', 'success')
        return redirect(url_for('crud'))


    
