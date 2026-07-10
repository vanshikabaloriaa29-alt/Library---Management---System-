from utils import books, issue_books

def issue():
    book_name = input("Enter the book name to issue : ").upper()
    if book_name in books:
        from datetime import datetime
        student = input("Enter Student Name: ")
        days = int(input("Enter number of days to issue the book : "))
        issue_books[book_name] = {
              "student": student,
              "date": datetime.now().date(),
              "days": days
              }
        del books[book_name]
        print(f"\n'{book_name}' has been assigned successfully to {student}. ")
        print("\nLate Fine Notice")
        print("1st week : Rs.10/day/book")
        print("2nd week : Rs.20/day/book")
        print("3rd week : Rs.60/day/book")
        print("After that fine will keep increasing.")
        
    else:
        print("\nSorry! The requested book is not available.")