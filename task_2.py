class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
        return self.movies
    
class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)  # Используем метод родительского класса
        return f"Комедии: {self.movies}"
    
class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)  # Используем метод родительского класса
        return f"Драмы: {self.movies}"
    
    
comedy = Comedy()
print(comedy.add_movie('Большой куш'))

drama = Drama()
print(drama.add_movie('Оружейный барон'))




