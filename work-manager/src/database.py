class Database:
    def __init__(self):
        self.employees = []

    def insert_employee(self, employee):
        self.employees.append(employee)

    def get_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        return next((emp for emp in self.employees if emp["id"] == emp_id), None)

    def delete_employee(self, emp_id):
        employee = self.get_employee(emp_id)
        if employee:
            self.employees.remove(employee)
            return True
        return False