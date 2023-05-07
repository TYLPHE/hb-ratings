"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
from jinja2 import StrictUndefined
import crud

app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """ Render homepage """

    return render_template('homepage.html')

@app.route('/movies')
def movies():
    """ Render movies page """

    movies = crud.get_movies()
    
    return render_template('movies.html', movies=movies)


@app.route('/movies/<movie_id>')
def movie_details(movie_id):
    """ Render movie details """

    details = crud.get_movie_details(movie_id)

    return render_template('movie_details.html', movie=details)

    
@app.route('/users')
def users():
    """ Render users page """

    users = crud.get_users()

    return render_template('users.html', users=users)


@app.route('/users/<user_id>')
def user_details(user_id):
    """ Render user details page """

    user = crud.get_user_details(user_id)
    ratings = crud.get_user_ratings(user_id)

    return render_template('user_details.html', user=user, ratings=ratings)


@app.route('/users', methods=['POST'])
def register_user():
    """ Create a new user """

    email = request.form.get('email')    
    password = request.form.get('password')
    email_exists = crud.get_user_by_email(email)

    if (email_exists):
        flash('User already exists.')
    else:
        new_user = crud.create_user(email, password)
        db.session.add(new_user)
        db.session.commit()
        flash('User created. Please log in.')

    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    """ Log the user in and redirect to homepage """

    email = request.form.get('email')
    password = request.form.get('password')
    login_ok = crud.check_login(email, password)

    if (login_ok):
        session['user_id'] = login_ok.user_id
        flash('Welcome. You are logged in.')
    else:
        flash('Incorrect email or password.')

    return redirect('/')


@app.route('/rating/<user_id>', methods=['POST'])
def add_rating(user_id):
    """ Adds logged in user's rating to database """

    rating = request.form.get('rating')
    movie_id = request.form.get('movie_id')
    new_rating = crud.handle_rating(user_id, rating, movie_id)
    print('@@@@@RATING: ', rating)
    db.session.add(new_rating)
    db.session.commit()
    
    return redirect(f'/users/{user_id}')

@app.route('/logout')
def logout():
    """ logs the user out and redirects to homepage """

    session.pop('user_id', None)
    
    return redirect('/')


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
