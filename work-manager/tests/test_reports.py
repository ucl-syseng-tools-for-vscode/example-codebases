import pytest
from src.reports import ReportManager
from src.database import Database

@pytest.fixture
def report_manager():
    return ReportManager(Database())

def test_generate_payroll_report(report_manager, capsys):
    report_manager.db.insert_employee({"id": 1, "name": "Charlie", "salary": 7000})
    report_manager.generate_payroll_report()
    captured = capsys.readouterr()
    assert "Payroll Report" in captured.out
