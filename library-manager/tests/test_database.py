import pytest
import os
from src.database import Database

TEST_FILE_PATH = "data/test_library_data.json"

@pytest.fixture
def database():
    db = Database()
    db.FILE_PATH = TEST_FILE_PATH  # Use a test file to avoid overwriting main data
    yield db
    if os.path.exists(TEST_FILE_PATH):
        os.remove(TEST_FILE_PATH)  # Cleanup test data after execution

def test_insert_book(database):
    book = {"id": 1, "title": "Moby Dick", "author": "Herman Melville", "borrowed": False}
    database.insert_book(book)
    assert len(database.get_books()) == 1

def test_insert_user(database):
    user = {"id": 1, "name": "Eve"}
    database.insert_user(user)
    assert len(database.get_users()) == 1

def test_insert_transaction(database):
    transaction = {"user_id": 1, "book_id": 2, "action": "borrow"}
    database.insert_transaction(transaction)
    assert len(database.get_transactions()) == 1

def test_persistence(database):
    """Test that data persists when saved to JSON."""
    book = {"id": 1, "title": "The Odyssey", "author": "Homer", "borrowed": False}
    database.insert_book(book)
    database.load_data()  # Simulate reloading the database
    assert len(database.get_books()) == 1
