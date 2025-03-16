import pytest
from src.database import Database

@pytest.fixture
def db():
    return Database()

def test_insert_expense(db):
    db.insert_expense(100, "Food", "Lunch")
    assert len(db.get_expenses()) == 1

def test_delete_nonexistent_expense(db):
    assert db.delete_expense(999)