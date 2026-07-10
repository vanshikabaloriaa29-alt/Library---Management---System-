from add_books import add
from issue_book import issue
from show_books import show
from return_book import return_book

def library():
    while True:
        print("\n------ Library Management ------")
        print("1. Add Book")
        print("2. Show Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        print("------------------------------------")
        choice = int(input("Enter your choice (1-5): "))
        
        if choice==1:   add()
        elif choice==2: show()
        elif choice==3: issue()
        elif choice==4: return_book()
        elif choice==5: 
            print("\nThank you for using the Library Management System. Have a nice day!")
            break
        else:
            print("\nInvalid choice! Please select a valid option.")
            
library()