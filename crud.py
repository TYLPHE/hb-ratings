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


if __name__ == '__main__':
    from server import app
    app.app_context().push()
    connect_to_db(app)
