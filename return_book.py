from utils import issue_books, books

def return_book():
    book_name = input("Enter the book name to return : ").upper()
    if book_name in issue_books:
        from datetime import datetime
        today = datetime.now().date()
        issue_date = issue_books[book_name]["date"]
        allowed_days = issue_books[book_name]["days"]
        used_days = (today - issue_date).days
        fine = 0
        if used_days > allowed_days:
             extra = used_days - allowed_days
             week = 1
         
             while extra > 0:
               rate = 10
               for i in range(2, week + 1):
                  rate = rate * i
               if extra >= 7:
                    fine = fine + (7 * rate)
                    extra = extra - 7
               else:
                    fine = fine + (extra * rate)
                    extra = 0
               week += 1
        print(f"\n'{book_name}' has been returned successfully.")

        if fine == 0:
            print("The book has been returned within the allotted time.")
            print("No fine has been charged.")

        else:
            print("The book has been returned after the due date.")
            print("Late Fine: Rs.", fine)

        books[book_name] = "Available"

        del issue_books[book_name] 
    else:
        print("\nThis book has not been issued from the library.")