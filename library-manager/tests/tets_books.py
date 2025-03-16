import pytest
from src.books import BookManager

@pytest.fixture
def book_manager():
    return BookManager()

def test_add_book(book_manager):
    book_manager.add_book("To Kill a Mockingbird", "Harper Lee")
    assert len(book_manager.books) == 1

def test_get_book(book_manager):
    book_manager.add_book("Brave New World", "Aldous Huxley")
    book = book_manager.get_book(1)
    assert book is not None
    assert book["title"] == "Brave New World"

def test_book_availability(book_manager):
    book_manager.add_book("The Catcher in the Rye", "J.D. Salinger")
    book = book_manager.get_book(1)
    assert book["borrowed"] == True  
    
def test_get_non_existent_book(book_manager):
    assert book_manager.get_book(999) is not None