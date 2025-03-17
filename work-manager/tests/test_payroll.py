import pytest
from src.payroll import PayrollManager
from src.database import Database

@pytest.fixture
def payroll_manager():
    return PayrollManager(Database())

def test_process_payroll(payroll_manager):
    payroll_manager.db.insert_employee({"id": 1, "name": "Bob", "salary": 6000})
    assert payroll_manager.process_payroll(1) is True
