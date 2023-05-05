""" Script to seed database """

import os, json, random, datetime, model, server, crud

# Commands to create a new 'ratings' db
os.system('dropdb ratings')
os.system('createdb ratings')
server.app.app_context().push()
model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
for movie in movie_data:
    t = movie['title']
    o = movie['overview']
    r = datetime.datetime.strptime(movie['release_date'], '%Y-%m-%d')
    p = movie['poster_path']
    
    to_lst = crud.create_movie(t, o, r, p)
    movies_in_db.append(to_lst)

users_in_db = []
for n in range(10):
    email = f'email{n}@test.com'
    password = 'test'

    to_lst = crud.create_user(email, password)
    users_in_db.append(to_lst)

model.db.session.add_all(movies_in_db + users_in_db)
model.db.session.commit()
