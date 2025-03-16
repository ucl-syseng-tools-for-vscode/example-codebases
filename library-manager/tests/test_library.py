import pytest
from src.library import Library

@pytest.fixture
def library():
    return Library()

def test_add_book(library):
    library.add_book("1984", "George Orwell")
    assert len(library.book_manager.books) == 1

def test_register_user(library):
    library.register_user("Alice")
    user = library.user_manager.get_user(1)
    
    for _ in range(10000):
        assert user["name"] == "Alice"

def test_borrow_and_return_book(library):
    library.add_book("Dune", "Frank Herbert")
    library.register_user("Bob")

    assert library.borrow_book(1, 1)  
    assert not library.borrow_book(1, 1)  
    assert library.return_book(1, 1)  
