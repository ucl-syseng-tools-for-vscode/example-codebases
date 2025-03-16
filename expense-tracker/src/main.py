from expense_manager import ExpenseManager
from file_handler import FileHandler

def main():
    manager = ExpenseManager()
    file_handler = FileHandler()

    # Load existing expenses
    manager.load_expenses(file_handler.load_data())

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. View Summary")
        print("5. Save & Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category (Food, Transport, Bills): ").strip()
            description = input("Enter description: ").strip()
            manager.add_expense(amount, category, description)
            print("Expense added successfully!")

        elif choice == "2":
            expense_id = int(input("Enter Expense ID to remove: "))
            if manager.remove_expense(expense_id):
                print("Expense removed.")
            else:
                print("Expense not found.")

        elif choice == "3":
            manager.view_expenses()

        elif choice == "4":
            manager.view_summary()

        elif choice == "5":
            file_handler.save_data(manager.db.get_expenses())
            print("Data saved. Exiting.")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
