class PayrollManager:
    def __init__(self, database):
        self.db = database

    def process_payroll(self, emp_id):
        """Processes salary payout."""
        emp = self.db.get_employee(emp_id)
        if emp is None:
            print("❌ Error: Employee not found.")  
            return False

        if emp["salary"] == 0:
            print("❌ Error: Employee has zero salary.")  
            return False

        print(f"✅ Payroll processed for {emp['name']}: ${emp['salary']}")
        return True
