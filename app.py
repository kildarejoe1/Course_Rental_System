from movie import Movie
from user import User


my_movie=Movie("Aliens","Sci-fi")
my_user=User("James")
my_user.movies.append(my_movie)
print(my_user)
print(my_user.movies)
