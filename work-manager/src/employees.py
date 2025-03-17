class EmployeeManager:
    def __init__(self, database):
        self.db = database

    def add_employee(self, name, salary):
        """Adds an employee."""
        if salary < 0:
            print("❌ Error: Salary cannot be negative.")  
            return
        employee = {"id": len(self.db.get_employees()) + 1, "name": name, "salary": salary}
        self.db.insert_employee(employee)

    def remove_employee(self, emp_id):
        """Removes an employee."""
        if not self.db.delete_employee(emp_id):
            print("❌ Error: Employee ID does not exist.")  

    def view_employees(self):
        """Displays all employees."""
        employees = self.db.get_employees()
        for emp in employees:
            print(f"{emp['id']}: {emp['name']} - ${emp['salary']}")
