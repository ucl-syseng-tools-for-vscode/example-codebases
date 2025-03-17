class PayrollManager:
    def __init__(self, database):
        self.db = database

    def process_payroll(self, emp_id):
        if not isinstance(emp_id, int) or emp_id <= 0:
            print("❌ Error: Invalid employee ID.")  
            return False

        emp = self.db.get_employee(emp_id)
        if emp is None:
            print("❌ Error: Employee not found.")  
            return False

        if emp["salary"] == 0:
            print("❌ Error: Employee has zero salary.")  
            return False

        if emp["salary"] > 500_000:
            print(f"⚠ Warning: Processing unusually high salary: ${emp['salary']}")

        print(f"✅ Payroll processed for {emp['name']}: ${emp['salary']}")
        return True

    def process_bulk_payroll(self, emp_ids):
        if not isinstance(emp_ids, list) or not all(isinstance(i, int) for i in emp_ids):
            print("❌ Error: Invalid employee IDs list.")  
            return False

        failed_ids = []
        for emp_id in emp_ids:
            if not self.process_payroll(emp_id):
                failed_ids.append(emp_id)

        if failed_ids:
            print(f"❌ Payroll failed for employees: {failed_ids}")
            return False
        return True
