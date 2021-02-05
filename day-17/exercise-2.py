def pretty_print(*args, **kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

movie = {
	"book": "The Giver",
	"author": "Lois Lowry",
	"year": 1993
}

pretty_print(publisher="Houghton Mifflin", **movie)