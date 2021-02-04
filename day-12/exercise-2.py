def print_show_info(show):
    title, seasons,initial_release = [show[k] for k in ('title','seasons','initial_release')]
    print(f"{title} ({initial_release}) - {seasons} seasons")

tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
   	"initial_release": 2008
}

print_show_info(tv_show)
