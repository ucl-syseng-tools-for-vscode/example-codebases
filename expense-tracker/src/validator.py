class Validator:
    VALID_CATEGORIES = {"Food", "Transport", "Bills"}

    def is_valid_amount(self, amount):
        return isinstance(amount, (int, float)) and amount > 0

    def is_valid_category(self, category):
        return category in self.VALID_CATEGORIES
