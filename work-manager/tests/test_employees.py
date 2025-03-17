import pytest
from src.employees import EmployeeManager
from src.database import Database

@pytest.fixture
def emp_manager():
    return EmployeeManager(Database())

def test_add_employee(emp_manager):
    emp_manager.add_employee("Alice", 5000)
    assert len(emp_manager.db.get_employees()) == 1
