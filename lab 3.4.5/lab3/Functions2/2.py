from dict import movies
def above_5_5_sublist(movies):
    return [movie['name'] for movie in movies if movie['imdb'] > 5.5]

print(above_5_5_sublist(movies))
