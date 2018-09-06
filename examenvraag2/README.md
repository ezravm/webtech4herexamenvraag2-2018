# Repo for Ezra's Spring exam


## Installation

1. Clone repo
2. install python and django
3. run using cli --> python manage.py runserver

## Usage 

navigate to localhost:8000/examen/filldb to add the movies to the redisdatabase
navigate to localhost:8000/examen/get_movies to get a list of all the movies in the database
navigate to http://localhost:8000/examen/search_movie?movie= to get a specific movie (if none is specified it falls back to saving private ryan)
for example http://localhost:8000/examen/search_movie?movie=The%20Godfather
