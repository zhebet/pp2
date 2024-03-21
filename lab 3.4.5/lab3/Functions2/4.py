from dict import movies
def average_imdb_score(movies):
    total_score = sum(movie['imdb'] for movie in movies)
    return total_score / len(movies)

# Test the function
print(average_imdb_score(movies))
