class ReportManager:
    def __init__(self, book_manager, user_manager, transaction_manager):
        self.book_manager = book_manager
        self.user_manager = user_manager
        self.transaction_manager = transaction_manager

    def most_borrowed_books(self):
        """Generates a report of the most borrowed books."""
        borrow_counts = {}

        for txn in self.transaction_manager.transactions:
            if txn["action"] == "borrow":
                book_id = txn["book_id"]
                borrow_counts[book_id] = borrow_counts.get(book_id, 0) + 1

        if not borrow_counts:
            print("\nNo books have been borrowed yet.")
            return

        sorted_books = sorted(borrow_counts.items(), key=lambda x: x[1], reverse=True)
        print("\nMost Borrowed Books:")
        for book_id, count in sorted_books[:5]:  # Show top 5 books
            book = self.book_manager.get_book(book_id)
            if book:
                print(f"{book['title']} by {book['author']} - Borrowed {count} times")

    def active_users(self):
        """Generates a report of users who borrowed the most books."""
        user_activity = {}

        for txn in self.transaction_manager.transactions:
            if txn["action"] == "borrow":
                user_id = txn["user_id"]
                user_activity[user_id] = user_activity.get(user_id, 0) + 1

        if not user_activity:
            print("\nNo users have borrowed books yet.")
            return

        sorted_users = sorted(user_activity.items(), key=lambda x: x[1], reverse=True)
        print("\nMost Active Users:")
        for user_id, count in sorted_users[:5]:  # Show top 5 users
            user = self.user_manager.get_user(user_id)
            if user:
                print(f"{user['name']} - Borrowed {count} books")

    def available_books(self):
        """Lists all available books."""
        print("\nAvailable Books:")
        for book in self.book_manager.books.values():
            if not book["borrowed"]:
                print(f"{book['title']} by {book['author']}")
