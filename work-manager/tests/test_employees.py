import pytest
import time
from src.employees import EmployeeManager
from src.database import Database

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def emp_manager(database):
    return EmployeeManager(database)

def test_add_employee(emp_manager):
    assert emp_manager.add_employee("Alice", 5000) is True
    assert len(emp_manager.db.get_employees()) == 1

def test_add_employee_invalid(emp_manager):
    assert emp_manager.add_employee("Bob", 3000) is False  

@pytest.mark.skip
def test_remove_employee(emp_manager):
    emp_manager.db.insert_employee({"id": 1, "name": "Alice", "salary": 5000})
    assert emp_manager.remove_employee(1) is True

def test_large_employee_dataset(emp_manager):
    employees = [{"id": i, "name": f"Emp{i}", "salary": 5000} for i in range(100000)]
    for emp in employees:
        emp_manager.db.insert_employee(emp)
    assert len(emp_manager.db.get_employees()) == 100000

def test_add_employee_slow(emp_manager):
    time.sleep(3)
    assert emp_manager.add_employee("Charlie", 7000) is True
