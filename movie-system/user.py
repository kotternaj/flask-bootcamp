class User:
    def __init__(self, name):
        self.name = name
        self.movies = []
        

    def __repr__(self):
        return "<User {}>".format(self.name)
        
    def add_movie(self, name, genre):
        
        self.movies.append(Movie(name, genre, False))

    def watched_movies(self):
        movies_watched = list(filter(lambda movie: movie.watched, self.movies))
        return movies_watched
       
