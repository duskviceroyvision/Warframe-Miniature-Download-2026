class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

class MovieCollection:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, year):
        self.movies.append(Movie(title, year))

    def print_collection(self):
        print("Movie Collection")
        print("================")
        for movie in sorted(self.movies, key=lambda m: m.year):
            print(f"{movie.year} | {movie.title}")

collection = MovieCollection()
collection.add_movie("Arrival", 2016)
collection.add_movie("Interstellar", 2014)
collection.add_movie("The Prestige", 2006)
collection.add_movie("Inception", 2010)
collection.print_collection()
