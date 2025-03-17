import pytest
import time
from src.reports import ReportManager
from src.database import Database

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def report_manager(database):
    return ReportManager(database)

def test_generate_payroll_report(report_manager, capsys):
    report_manager.db.insert_employee({"id": 1, "name": "Charlie", "salary": 7000})
    report_manager.generate_payroll_report()
    captured = capsys.readouterr()
    assert "Payroll Report" in captured.out
    assert "Charlie: $7000" in captured.out

def test_generate_empty_payroll_report(report_manager, capsys):
    report_manager.generate_payroll_report()
    captured = capsys.readouterr()
    assert "No employees in the system" in captured.out

def test_generate_report_slow(report_manager):
    report_manager.db.employees = [{"id": i, "name": f"Employee{i}", "salary": 5000} for i in range(30000)]
    time.sleep(4)  
    report_manager.generate_payroll_report()
