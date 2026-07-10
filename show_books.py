from utils import books
def show():
    if len(books)==0:
        print("\nBooks are currently not available in the library.")
    else:
        print("\nAvailable Books")
        print("------------------")
        for book in books:
            print(book)