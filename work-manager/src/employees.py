class EmployeeManager:
    def __init__(self, database):
        self.db = database

    def add_employee(self, name, salary):
        if not isinstance(name, str) or not name.strip():
            print("❌ Error: Employee name must be a non-empty string.")  
            return False
        
        if not isinstance(salary, (int, float)) or salary < 0:
            print("❌ Error: Salary must be a positive number.")  
            return False
        
        if any(emp["name"] == name for emp in self.db.get_employees()):
            print("❌ Error: Employee with the same name already exists.")  
            return False

        if salary > 1_000_000:
            print("⚠ Warning: Unusually high salary detected.")

        employee = {"id": len(self.db.get_employees()) + 1, "name": name, "salary": salary}
        self.db.insert_employee(employee)
        return True

    def remove_employee(self, emp_id):
        if not isinstance(emp_id, int) or emp_id <= 0:
            print("❌ Error: Invalid employee ID.")  
            return False

        if not self.db.delete_employee(emp_id):
            print("❌ Error: Employee ID does not exist.")  
            return False
        return True

    def view_employees(self):
        employees = self.db.get_employees()
        if not employees:
            print("❌ No employees found.")
            return
        for emp in employees:
            print(f"{emp['id']}: {emp['name']} - ${emp['salary']}")
