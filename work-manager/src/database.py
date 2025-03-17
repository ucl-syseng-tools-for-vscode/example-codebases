import json
import os

class Database:
    FILE_PATH = "data/employees.json"

    def __init__(self):
        self.data = {"employees": []}
        self.load_data()

    def load_data(self):
        """Loads employee data from a JSON file."""
        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "r") as f:
                self.data = json.load(f)

    def save_data(self):
        """Saves current data to a JSON file."""
        os.makedirs("data", exist_ok=True)
        with open(self.FILE_PATH, "w") as f:
            json.dump(self.data, f, indent=4)

    def insert_employee(self, employee):
        """Adds an employee."""
        self.data["employees"].append(employee)
        self.save_data()

    def get_employees(self):
        """Returns all employees."""
        return self.data["employees"]

    def get_employee(self, emp_id):
        """Finds an employee by ID."""
        return next((e for e in self.data["employees"] if e["id"] == emp_id), None)

    def delete_employee(self, emp_id):
        """Deletes an employee."""
        employees = self.data["employees"]
        for emp in employees:
            if emp["id"] == emp_id:
                employees.remove(emp)
                self.save_data()
                return True
        return False
