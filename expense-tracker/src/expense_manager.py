from database import Database
from validator import Validator

class ExpenseManager:
    def __init__(self):
        self.db = Database()
        self.validator = Validator()

    def add_expense(self, amount, category, description):
        """Adds an expense after validation."""
        if not self.validator.is_valid_amount(amount):
            return False
        if not self.validator.is_valid_category(category):
            return False
        self.db.insert_expense(amount, category, description)
        return True

    def remove_expense(self, expense_id):
        """Removes an expense."""
        return self.db.delete_expense(expense_id)

    def view_expenses(self):
        """Returns stored expenses."""
        return self.db.get_expenses()

    def view_summary(self):
        """Returns a summary of expenses by category."""
        return self.db.get_summary()

    def load_expenses(self, expense_data):
        """Loads expenses from a file."""
        self.db.load_expenses(expense_data)
