class BookManager:
    def __init__(self):
        self.books = {}
        self.next_id = 1

    def add_book(self, title, author):
        """Adds a new book but does NOT prevent duplicate titles."""
        for book in self.books.values():
            if book["title"].lower() == title.lower():
                print(f"❌ Warning: Duplicate title '{title}'")  
                return

        book = {"id": self.next_id, "title": title, "author": author, "borrowed": False}
        self.books[self.next_id] = book
        self.next_id += 1

    def get_book(self, book_id):
        """Retrieves a book, but allows searching for invalid book IDs."""
        if book_id not in self.books:
            print(f"❌ Error: Book ID {book_id} does not exist") 
        return self.books.get(book_id, None)

    def view_books(self):
        print("\nBooks in Library:")
        for book in self.books.values():
            status = "Borrowed" if book["borrowed"] else "Available"
            print(f"{book['id']}: {book['title']} by {book['author']} ({status})")
