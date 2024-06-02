class Film:

    def __init__(self, title, genre, director, year, duration, company, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.company = company
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.year} {self.company})"


class FilmModel:
    def __init__(self):
        self.films = {}

    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.films[film.title] = film

    def get_all_films(self):
        return self.films.values()

    def get_single_film(self, user_title):
        film = self.films[user_title]
        dict_film = {
            "название": film.title,
            "жанр": film.genre,
            "режиссёр": film.director,
            "год": film.year,
            "длительность": film.duration,
            "студия": film.company,
            "актеры": film.actors
        }
        return dict_film

    def remove_film(self, user_title):
        return self.films.pop(user_title)
