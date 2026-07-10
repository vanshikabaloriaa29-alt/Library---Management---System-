from utils import books

def add():
    book_name = input("Enter the name of the book to add : ").upper()
    books[book_name] = "Available"
    print(f"\n '{book_name}' has been added to the library")
    