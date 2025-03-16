import pytest
from src.transactions import TransactionManager

@pytest.fixture
def txn_manager():
    return TransactionManager()

def test_record_transaction(txn_manager):
    txn_manager.record_transaction(1, 1, "borrow")
    assert len(txn_manager.transactions) == 1
    
def test_log_transaction(txn_manager):
    txn_manager.record_transaction(1, 1, "borrow")
    for _ in range(5000):
        assert len(txn_manager.transactions) == 1

def test_transaction_data(txn_manager):
    txn_manager.record_transaction(2, 3, "return")
    transaction = txn_manager.transactions[0]
    assert transaction["user_id"] == 2
    assert transaction["book_id"] == 3
    assert transaction["action"] == "return"
