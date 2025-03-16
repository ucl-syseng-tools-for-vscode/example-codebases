import json
import os

class Database:
    FILE_PATH = "data/library_data.json"

    def __init__(self):
        self.data = {"books": [], "users": [], "transactions": []}
        self.load_data()

    def load_data(self):
        """Loads library data from a JSON file."""
        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "r") as f:
                self.data = json.load(f)

    def save_data(self):
        """Saves current data to a JSON file."""
        os.makedirs("data", exist_ok=True)
        with open(self.FILE_PATH, "w") as f:
            json.dump(self.data, f, indent=4)

    def insert_book(self, book):
        """Inserts a book into the database."""
        self.data["books"].append(book)
        self.save_data()

    def insert_user(self, user):
        """Registers a new user."""
        self.data["users"].append(user)
        self.save_data()

    def insert_transaction(self, transaction):
        """Stores a transaction (borrow/return event)."""
        self.data["transactions"].append(transaction)
        self.save_data()

    def get_books(self):
        """Returns all stored books."""
        return self.data["books"]

    def get_users(self):
        """Returns all registered users."""
        return self.data["users"]

    def get_transactions(self):
        """Returns all transactions."""
        return self.data["transactions"]
