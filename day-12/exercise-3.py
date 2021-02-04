def print_show_info(show):
	print(
		f"{show['title']} ({show['initial_release']}) - {show['seasons']} season(s)")


series_data = [
	{"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
	{"title": "Fargo", "seasons": 4, "initial_release": 2014},
	{"title": "Firefly", "seasons": 1, "initial_release": 2002},
	{"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
	{"title": "True Detective", "seasons": 3, "initial_release": 2014},
	{"title": "Westworld", "seasons": 3, "initial_release": 2016},
]

for show in series_data:
	print_show_info(show)
