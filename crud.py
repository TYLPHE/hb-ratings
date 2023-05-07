""" CRUD operations """

# Leaving smelly comment below for learning 
# from model import User, Movie, Rating, db, connect_to_db
from model import *

def create_user(email, password):
    """ Create and return new user """

    user = User(email=email, password=password)

    return user


def create_movie(title, overview, release_date, poster_path):
    """ Create and return new movie """

    movie = Movie(
        title=title,
        overview=overview,
        release_date=release_date,
        poster_path=poster_path,
    )

    return movie


def create_rating(score, user, movie):
    """ Create and return rating """

    rating = Rating(score=score, user=user, movie=movie)

    return rating


def get_movies():
    """ Returns a list of all movies """
    
    return Movie.query.all()


def get_movie_details(id):
    """ Returns Movie class """

    return Movie.query.filter_by(movie_id=id).first()


def get_users():
    """ Returns list of all users """

    return User.query.all()


def get_user_details(id):
    """ Returns a User class """

    return User.query.get(id)


def get_user_ratings(id):
    """ Returns a list of user's ratings """

    return Rating.query.filter(Rating.user_id == id).all()


def get_user_by_email(email):
    """ Return a user by email """

    return User.query.filter(User.email ==email).first()


def check_login(email, password):
    """ Check database if email and password match """

    return User.query.filter(User.email==email, User.password==password).first()


def handle_rating(user_id, rating, movie_id):
    """ Retrieve parameters as strings and query database to add new rating """

    user = User.query.get(user_id)
    movie = Movie.query.get(movie_id)

    return create_rating(rating, user, movie)


if __name__ == '__main__':
    from server import app
    app.app_context().push()
    connect_to_db(app)
