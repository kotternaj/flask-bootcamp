from movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []
        

    def __repr__(self):
        return "<User {}>".format(self.name)
        
    def add_movie(self, name, genre):        
        self.movies.append(Movie(name, genre, False))

    def delete(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        movies_watched = list(filter(lambda movie: movie.watched, self.movies))
        return movies_watched
       
    def json(self):
        return {
            'name': self.name, 
            'movies': [
                movies.json() for movie in self.movies
            ]
        }
    
    @classmethod
    def from_json(cls, json_data):
        user = User(json_data['name'])
        movies = []
        for movie in json_data['movies']:
            movies.append(Movie(movie['name'], movie['genre'], movie['watched']))
        user.movies = movies

        return user

