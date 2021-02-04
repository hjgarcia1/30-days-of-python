movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

for i in range(2):
    user_movie = input("Enter two movies and their budgets: ").strip()
    movie = user_movie.split(" ")
    movie_name = (" ").join(movie[0:-1])
    movies.append(tuple([movie_name, int(movie[-1])]))

total = 0

for movie in movies:
    total += movie[1]

average = total/len(movies)

for movie in movies:
    if(movie[1] > average):
        overage = movie[1] - average
        print(f"{movie[0]} is ${overage:,} over the average.")