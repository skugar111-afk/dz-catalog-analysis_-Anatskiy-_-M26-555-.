import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", 
     "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
] 

def average_rating(movies):
    n = 0
    for movie in movies:
        n += float(movie['rating'])
    avg = n / len(movies)
    return round(avg, 1)


def catalog_age_stats(movies, current_year=2026):
    ages = []
    for movie in movies:
        year = int(movie['year'])
        age = current_year - year
        ages.append(age)
    oldest = max(ages)         
    newest = min(ages)         
    avg_age = sum(ages) / len(ages)
    avg_age_ceil = math.ceil(avg_age)
    return (oldest, newest, avg_age_ceil)


def duration_in_hours(minutes):
    hours = minutes // 60
    minutes_ = minutes % 60
    return f"{hours}ч {minutes_}м"


def rating_tier(rating):
    if rating >= 9:
        return 'шедевр'
    elif rating >= 7:
        return 'хорошо'
    elif rating >= 5:
        return "средне" if rating < 7 else "хорошо"
    else:
        return "слабо"

def decade_label(year):
    match year:
        case year if year > 2000:
            return 'новые'
        case year if (year >= 2015 and year <= 2020):
            return 'недавние'
        case year if year < 2015:
            return 'старые'
   
for movie in movies:
    if "comedy" not in movie["genres"]:
        print(movie["title"])
    else:
        continue

for movie in movies:
    if movie['rating'] <= 8.0:
        continue
    print(movie['title'])
    break
else:
    print('Шедевров нет')


def count_long_movies(movies, threshold=120):
    n = 0
    for movie in movies:
        if movie['duration_min'] > threshold:
            n += 1
    return n


def normalize_title(title):
    words = title.split()
    result_words = []
    for word in words:
        if len(word) == 0:
            result_words.append(word)
        else:
            new_word = word[0].upper() + word[1:]
            result_words.append(new_word)
    return ' '.join(result_words)

def make_slug(title):
    title = title.lower()
    slug = title.replace(' ', '-')
    return slug

def format_report_line(movie):
    return f'"{movie["title"]}" ({movie["year"]}) —'
    f'{movie["rating"]}/10,{duration_in_hours(int(movie["duration_min"]))},'
    f'жанры: {", ".join(movie["genres"])}'


def titles_sorted_by_rating(movies):
    return [movie['title'] for movie in sorted(movies, key=lambda x: x['rating'])]

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda x: x['rating'], reverse=True)[:n]
    result = []
    for movie in sorted_movies:
        result.append((movie['title'], movie['rating']))
    return result


def count_by_genre(movies):
    genre_counts = {}
    for movie in movies:
        for genre in movie['genres']:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie['actors']:
            if actor not in filmography:
                filmography[actor] = []
                filmography[actor].append(movie['title'])
    return filmography


def above_average_ratings(movies):
    avg = average_rating(movies)
    return {m['title']: m['rating'] for m in movies if m['rating'] > avg}
                              
                              
def all_genres(movies):
    genres = set() 
    for movie in movies:
        for genre in movie['genres']:
            genres.update(movie['genres'])
    return genres

def common_actors(movie1, movie2):
    return set(movie1['actors']) & set(movie2['actors'])

def genres_only_in_one(movies_a, movies_b):                 
    return set(movies_a['genres']) - set(movies_b['genres'])

def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if float(movie['rating']) >= min_rating:
            yield movie

for movie in iter_high_rated(movies):
    print(format_report_line(movie))

def build_report(movies):

    print("=== ОБЩАЯ СТАТИСТИКА ===")
    print()
    print(f"Средний рейтинг: {average_rating(movies)}")
    print()
    oldest, newest, avg_age_ceil = catalog_age_stats(movies)
    print("Средний возраст фильма:", avg_age_ceil)
    print()
    print("Топ-3 фильма:")
    for title, rating in top_n_by_rating(movies, n=3):
        print(f"{title} — {rating}/10")
    print()
    print('Фильм по жанрам')
    print()
    print(count_by_genre(movies))
    print()
    print('Все жанры каталога:')
    print(', '.join(all_genres(movies)))

build_report(movies)