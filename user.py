
class User:
    def __init__(self,name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {} and list is {} > ".format(self.name, self.movies)

    def watched_movies(self):
        movies_watched= list(filter(lambda movie: movie.watched, self.movies))
        return movies_watched
