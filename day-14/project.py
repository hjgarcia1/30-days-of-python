import csv
import os.path

books = []
file_exists = os.path.isfile("./day-14/book_data.csv")
FIELDS = ["title", "author", "publication_year","read"]


def print_book_info(books):
    for book in books:
        print()
        print(f"{book['title']} by {book['author']} - {book['publication_year']} - {book['read']}")
        print()


def get_all_books():
    with open("./day-14/book_data.csv", "r") as file:
        return list(csv.DictReader(file))


def create_book():
    title = input("What is the title of the book: ").strip()
    author = input("What is the author of the book: ").strip()
    year = input("What is the year of publication: ").strip()

    with open("./day-14/book_data.csv", "a", newline='') as book_file:
        writer = csv.DictWriter(book_file, FIELDS)

        if not file_exists:
            writer.writeheader()

        writer.writerow({"title": title, "author": author,
                         "publication_year": year, "read":"Not Read"})


def search_books():
    searchTerm = input("Search: ").strip().lower()
    matching_books = []

    books = get_all_books()

    for book in books:
        if(searchTerm in book['title'].lower()):
            matching_books.append(book)

    return matching_books


def delete_book():
    title = input("Enter the book title you would like to delete: ").strip().lower()

    books = get_all_books()

    for book in books:
        if(title != book['title'].lower()):

            with open("./day-14/book_data.csv", "w", newline='') as book_file:
                writer = csv.DictWriter(book_file, FIELDS)

                writer.writeheader()

                if(title != book['title'].lower()):
                    writer.writerow({"title": book['title'], "author": book["author"],
                                     "publication_year": book["publication_year"],"read":book["read"]})
    else:
        print("No Book was found")

def mark_as_read():

    title = input(
        "Enter the title of the book you would like to mark as read: ").strip().lower()

    books = get_all_books()

    for book in books:
        with open("./day-14/book_data.csv", "w", newline='') as book_file:
            writer = csv.DictWriter(book_file, FIELDS)

            writer.writeheader()

            if(title != book['title'].lower()):
                writer.writerow({"title": book['title'], "author": book["author"],
                                 "publication_year": book["publication_year"], "read":book["read"]})
            else:
                writer.writerow({"title": book['title'], "author": book["author"],
                                 "publication_year": book["publication_year"], "read":"Read"})

while True:

    menu_prompt = """Please enter one of the following options:

    - 'a' to add a book
    - 'l' to list the books
    - 'd' to delete a book
    - 's' to search for a book
    - 'r' mark book as read
    - 'q' to quit

    What would you like to do? """

    selected_option = input(menu_prompt)

    if selected_option == "l":
        books = get_all_books()

        if books:
            print_book_info(books)
        else:
            print("No books available you will need to create one.")

    elif selected_option == "a":
        create_book()

    elif selected_option == "d":
        delete_book()

    elif selected_option == "r":
        mark_as_read()

    elif selected_option == "s":
        books = search_books()

        if books:
            print_book_info(books)
        else:
            print("No books found.")

    elif selected_option == "q":
        print("You selected option 'q'! Quitting the menu!")
        break

    else:
        print("You selected an invalid option.")
