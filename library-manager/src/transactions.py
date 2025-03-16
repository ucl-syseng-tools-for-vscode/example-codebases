class TransactionManager:
    def __init__(self):
        self.transactions = []

    def record_transaction(self, user_id, book_id, action):
        self.transactions.append({"user_id": user_id, "book_id": book_id, "action": action})

    def view_transactions(self):
        print("\nLibrary Transactions:")
        for txn in self.transactions:
            print(f"User {txn['user_id']} {txn['action']} Book {txn['book_id']}")
