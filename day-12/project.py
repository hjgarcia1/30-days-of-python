books = []


def print_book_info(book):
    print(f"{book['title']} by {book['author']} - {book['publication_year']}.")


def diplay_books(books):
    if not books:
        print("Book list empty, please use option \"b\" to add to the books list")
        return
    for book in books:
        print_book_info(book)


def create_book():
    title = input("What is the title of the book: ").strip()
    author = input("What is the author of the book: ").strip()
    year = input("What is the year of publication: ").strip()

    book_info = {
        "title": title,
        "author": author,
        "publication_year": int(year)
    }

    books.append(book_info)


while True:
    selected_option = input(
        "Please enter 'a' to view all books, 'b' to enter a books, or enter 'q' to quit: ")
    if selected_option == "a":
        diplay_books(books)
    elif selected_option == "b":
        create_book()
    elif selected_option == "q":
        print("You selected option 'q'! Quitting the menu!")
        break
    else:
        print("You selected an invalid option.")
