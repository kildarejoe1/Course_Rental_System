
class User:
    def __init__(self,name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {} and list is {} > ".format(self.name, self.movies)

    def print_movie(self):
        print("User {} as a list of movies which are: ".format(self.name))
        for movie_name in self.movies.name:
            print(movie_name)
