from dict import movies
def movies_by_category(movies, category):
    return [movie['name'] for movie in movies if movie['category'] == category]


category = "Romance"
print(movies_by_category(movies, category))
