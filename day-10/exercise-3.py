album = {
    "Album":   "The Dark Side of the Moon",
    "Artist": "Pink Floyd",
    "Year": 1973,
    "Tracks":   (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
}

album.pop("Year")
album.pop("Tracks")

album["release_date"] = "March 1st, 1973"

# print(album["Tracks"])
print(album.get("Tracks"))
