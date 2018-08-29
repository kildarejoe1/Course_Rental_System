from movie import Movie
class User:
    def __init__(self,name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {} and list is {} > ".format(self.name, self.movies)

    def watched_movies(self):
        movies_watched= list(filter(lambda movie: movie.watched, self.movies))
        return movies_watched

    def add_movie(self,name,genre): #my_user_object
        movie = Movie(name,genre, False)
        self.movies.append(movie)

    def remove_movie(self,movie_name):
        for movie in self.movies:
            if movie.name == movie_name:
                self.movies.remove(movie)

    def save_to_file(self):
        with open(self.name+".txt", "w") as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write(movie.name + "," + movie.genre + "," + str(movie.watched)+"\n")

    @classmethod
    def load_from_file(cls,filename):
        with open(filename, "r") as f:
            content=f.readlines()
            username=content[0]
            movies = []
            for line in content[1:]:
                movie_data = line.split(",") #"name" genre "watches"
                movies.append(Movie(movie_data[0],movie_data[1],movie_data[2] == "True"))
            user = User(username)
            user.movies = movies
            return user

    def json(self):
        return {
        "name" : self.name,
        "movies" : [movie.json()  for movie in self.movies ]
        }
