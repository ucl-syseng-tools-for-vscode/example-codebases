class ReportManager:
    def __init__(self, database):
        self.db = database

    def generate_payroll_report(self):
        """Generates a payroll report."""
        employees = self.db.get_employees()
        if not employees:
            print("❌ No employees in the system.")  
            return
        
        print("\nPayroll Report:")
        for emp in employees:
            print(f"{emp['name']}: ${emp['salary']}")
