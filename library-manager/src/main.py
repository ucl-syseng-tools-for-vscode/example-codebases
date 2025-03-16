from library import Library

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Register User")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. View Users")
        print("7. View Transactions")
        print("8. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            library.add_book(title, author)
        elif choice == "2":
            name = input("Enter user name: ")
            library.register_user(name)
        elif choice == "3":
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            library.borrow_book(user_id, book_id)
        elif choice == "4":
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            library.return_book(user_id, book_id)
        elif choice == "5":
            library.view_books()
        elif choice == "6":
            library.view_users()
        elif choice == "7":
            library.view_transactions()
        elif choice == "8":
            print("Exiting Library System.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
