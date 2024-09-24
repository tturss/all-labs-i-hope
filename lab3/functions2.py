# Task 1: 
def is_highly_rated(movie):
    return movie['imdb'] > 5.5

# Task 2: 
def get_highly_rated_movies(movies):
    return [movie for movie in movies if is_highly_rated(movie)]

# Task 3: 
def get_movies_by_category(movies, category):
    return [movie for movie in movies if movie['category'] == category]

# Task 4:
def get_average_imdb(movies):
    total_imdb = sum(movie['imdb'] for movie in movies)
    return total_imdb / len(movies) if movies else 0

# Task 5:
def get_average_imdb_by_category(movies, category):
    category_movies = get_movies_by_category(movies, category)
    return get_average_imdb(category_movies)


movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

print("Check if a movie's IMDB score is above 5.5")
print(f"Is 'Usual Suspects' highly rated? {'Yes' if is_highly_rated(movies[1]) else 'No'}\n")

print("list of movies with an IMDB score above 5.5")
highly_rated_movies = get_highly_rated_movies(movies)
for movie in highly_rated_movies:
    print(f"{movie['name']} (IMDB: {movie['imdb']})")
print()

print("List of Romance movies")
romance_movies = get_movies_by_category(movies, "Romance")
for movie in romance_movies:
    print(f"{movie['name']} (IMDB: {movie['imdb']})")
print()

print("Average IMDB score of all movies")
average_imdb_all = get_average_imdb(movies)
print(f"Average IMDB score: {average_imdb_all}\n")

print("Average IMDB score of Romance movies")
average_imdb_romance = get_average_imdb_by_category(movies, "Romance")
print(f"Average IMDB score for Romance movies: {average_imdb_romance}")
