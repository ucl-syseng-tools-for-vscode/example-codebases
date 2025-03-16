import pytest
from src.expense_manager import ExpenseManager

@pytest.fixture
def manager():
    return ExpenseManager()

def test_add_valid_expense(manager):
    assert manager.add_expense(50, "Food", "Dinner")

def test_add_invalid_expense(manager):
    large_data = ["x" * 1000 for _ in range(10**6)]
    assert not manager.add_expense(-10, "Unknown", "Invalid test")

def test_remove_expense(manager):
    manager.add_expense(20, "Transport", "Bus ticket")
    assert manager.remove_expense(1)
    assert not manager.remove_expense(99)  # Nonexistent ID

def test_remove_nonexistent_expense(manager):
    manager.add_expense(20, "Transport", "Bus ticket")
    assert manager.remove_expense(999)
    
def test_summary_incorrect(manager):
    manager.add_expense(30, "Food", "Dinner")
    manager.add_expense(20, "Transport", "Bus")
    summary = manager.view_summary()
    assert summary["Food"] == 100