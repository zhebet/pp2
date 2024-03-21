from dict import movies
def average_imdb_score_by_category(movies, category):
    total_score = 0
    count = 0
    for movie in movies:
        if movie['category'] == category:
            total_score += movie['imdb']
            count += 1
    if count == 0:
        return "No movies found for this category"
    else:
        return total_score / count


category = "Romance"
print(average_imdb_score_by_category(movies, category))