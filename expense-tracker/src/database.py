class Database:
    def __init__(self):
        self.expenses = []
        self.next_id = 1

    def insert_expense(self, amount, category, description):
        """Adds an expense."""
        expense = {"id": self.next_id, "amount": amount, "category": category, "description": description}
        self.expenses.append(expense)
        self.next_id += 1

    def delete_expense(self, expense_id):
        """Deletes an expense."""
        for exp in self.expenses:
            if exp["id"] == expense_id:
                self.expenses.remove(exp)
                return True
        return False

    def get_expenses(self):
        """Returns expenses."""
        return self.expenses

    def get_summary(self):
        """Summarizes expenses."""
        summary = {}
        for exp in self.expenses:
            summary[exp["category"]] = summary.get(exp["category"], 0) + exp["amount"]
        return summary

    def load_expenses(self, expense_data):
        """Loads expenses from a file."""
        self.expenses = expense_data
        self.next_id = max([exp["id"] for exp in self.expenses], default=0) + 1
