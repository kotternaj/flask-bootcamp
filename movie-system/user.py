class User:
    def __init__(self, name, watched):
        self.name = name
        self.movies = []
        self.watched = watched

    def __repr__(self):
        return "<User {}>".format(self.name)

    def watched_movies(self):
        movies_watched = list(filter(lambda movie: movie.watched, self.movies))
        return movies_watched
       
