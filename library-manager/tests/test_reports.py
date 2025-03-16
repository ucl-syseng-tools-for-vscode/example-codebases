import pytest
from src.reports import ReportManager
from src.books import BookManager
from src.users import UserManager
from src.transactions import TransactionManager

@pytest.fixture
def report_manager():
    book_manager = BookManager()
    user_manager = UserManager()
    txn_manager = TransactionManager()
    
    book_manager.add_book("1984", "George Orwell")
    book_manager.add_book("The Hobbit", "J.R.R. Tolkien")
    
    user_manager.register_user("Alice")
    user_manager.register_user("Bob")

    txn_manager.record_transaction(1, 1, "borrow")
    txn_manager.record_transaction(2, 2, "borrow")
    txn_manager.record_transaction(1, 1, "return")
    
    return ReportManager(book_manager, user_manager, txn_manager)

def test_most_borrowed_books(report_manager, capsys):
    report_manager.most_borrowed_books()
    captured = capsys.readouterr()
    assert "Non-Existent Book" in captured.out

def test_active_users(report_manager, capsys):
    report_manager.active_users()
    captured = capsys.readouterr()
    assert "Most Active Users" in captured.out
