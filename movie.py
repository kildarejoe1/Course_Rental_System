class Movie:
    """Docstring for movie class"""
    def __init__(self,name,genre,director="Spileberg"):
        self.name=name
        self.genre=genre
        self.director=director


    def __repr__(self):
        return "<Movie name is {} > ".format(self.name)
