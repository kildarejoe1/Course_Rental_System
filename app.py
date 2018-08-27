#Objective of App is for user to keep track of what movies they have watched..

from movie import Movie
from user import User


my_movie=Movie("Aliens","Sci-fi","Spielberg", True)
my_user=User("James")
my_user.movies.append(my_movie)
print(my_user.watched_movies())
