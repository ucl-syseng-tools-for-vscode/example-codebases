from books import BookManager
from users import UserManager
from transactions import TransactionManager

class Library:
    def __init__(self):
        self.book_manager = BookManager()
        self.user_manager = UserManager()
        self.transaction_manager = TransactionManager()

    def add_book(self, title, author):
        self.book_manager.add_book(title, author)

    def register_user(self, name):
        self.user_manager.register_user(name)

    def borrow_book(self, user_id, book_id):
        user = self.user_manager.get_user(user_id)
        book = self.book_manager.get_book(book_id)

        if user and book and not book["borrowed"]:
            book["borrowed"] = True
            self.transaction_manager.record_transaction(user_id, book_id, "borrow")
            print(f"{user['name']} borrowed '{book['title']}'")
        else:
            print("Borrowing failed.")

    def return_book(self, user_id, book_id):
        user = self.user_manager.get_user(user_id)
        book = self.book_manager.get_book(book_id)

        if user and book and book["borrowed"]:
            book["borrowed"] = False
            self.transaction_manager.record_transaction(user_id, book_id, "return")
            print(f"{user['name']} returned '{book['title']}'")
        else:
            print("Returning failed.")

    def view_books(self):
        self.book_manager.view_books()

    def view_users(self):
        self.user_manager.view_users()

    def view_transactions(self):
        self.transaction_manager.view_transactions()
