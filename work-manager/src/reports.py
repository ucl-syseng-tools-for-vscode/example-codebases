class ReportManager:
    def __init__(self, database):
        self.db = database

    def generate_payroll_report(self):
        employees = self.db.get_employees()
        if not employees:
            print("❌ No employees in the system.")  
            return

        print("\nPayroll Report:")
        for emp in employees:
            print(f"{emp['name']}: ${emp['salary']}")

    def generate_summary_report(self):
        employees = self.db.get_employees()
        if not employees:
            print("❌ No employees in the system.")  
            return

        total_salary = sum(emp["salary"] for emp in employees)
        avg_salary = total_salary / len(employees)
        highest_paid = max(employees, key=lambda x: x["salary"])
        lowest_paid = min(employees, key=lambda x: x["salary"])

        print("\nSalary Summary Report:")
        print(f"Total Salary: ${total_salary}")
        print(f"Average Salary: ${avg_salary:.2f}")
        print(f"Highest Paid: {highest_paid['name']} - ${highest_paid['salary']}")
        print(f"Lowest Paid: {lowest_paid['name']} - ${lowest_paid['salary']}")
