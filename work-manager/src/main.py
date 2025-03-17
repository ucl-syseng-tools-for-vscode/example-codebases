from employees import EmployeeManager
from payroll import PayrollManager
from reports import ReportManager
from database import Database

def main():
    db = Database()
    emp_manager = EmployeeManager(db)
    payroll = PayrollManager(db)
    reports = ReportManager(db)

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Process Payroll")
        print("4. View Employees")
        print("5. Generate Reports")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter employee name: ")
            salary = float(input("Enter salary: "))
            emp_manager.add_employee(name, salary)
        elif choice == "2":
            emp_id = int(input("Enter employee ID to remove: "))
            emp_manager.remove_employee(emp_id)
        elif choice == "3":
            emp_id = int(input("Enter employee ID for payroll: "))
            payroll.process_payroll(emp_id)
        elif choice == "4":
            emp_manager.view_employees()
        elif choice == "5":
            reports.generate_payroll_report()
        elif choice == "6":
            print("Exiting Employee Management System.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
