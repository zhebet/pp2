from dict import movies

def above_5_5(movie):
    return movie['imdb'] > 5.5


movie = {
    "name": "Usual Suspects",
    "imdb": 7.0,
    "category": "Thriller"
}
print(above_5_5(movie))  
