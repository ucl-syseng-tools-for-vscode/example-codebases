import pytest
import time
from src.payroll import PayrollManager
from src.database import Database

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def payroll_manager(database):
    return PayrollManager(database)

def test_process_payroll(payroll_manager):
    payroll_manager.db.insert_employee({"id": 1, "name": "Bob", "salary": 6000})
    assert payroll_manager.process_payroll(1) is True

def test_process_payroll_fails(payroll_manager):
    payroll_manager.db.insert_employee({"id": 2, "name": "Dave", "salary": 0})
    assert payroll_manager.process_payroll(2) is True  

def test_process_payroll_nonexistent(payroll_manager):
    assert payroll_manager.process_payroll(99) is False

def test_process_payroll_slow(payroll_manager):
    payroll_manager.db.insert_employee({"id": 3, "name": "Eve", "salary": 10000})
    time.sleep(5) 
    assert payroll_manager.process_payroll(3) is True

def test_process_large_dataset(payroll_manager):
    payroll_manager.db.employees = [{"id": i, "name": f"Employee{i}", "salary": 5000} for i in range(50000)]
    assert payroll_manager.process_payroll(25000) is True
