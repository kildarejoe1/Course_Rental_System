
class User:
    def __init__(self,name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {} and list is {} > ".format(self.name, self.movies)

    def watched_movies(self):
        movies_watched= list(filter(lambda movie: movie.watched, self.movies))
        return movies_watched

    def add_movie(self,name,director, genre): #my_user_object
        movie = Movie(name,genre, False)
        self.movies.append(movie)

    def remove_movie(self,movie_name):
        for movie in self.movies:
            if movie.name == movie_name:
                self.movies.remove(movie)
