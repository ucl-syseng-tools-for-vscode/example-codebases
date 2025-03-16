import json
import os

class FileHandler:
    FILE_PATH = "data/expenses.json"

    def load_data(self):
        """Loads expense data from JSON file."""
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, "r") as f:
            return json.load(f)

    def save_data(self, data):
        """Saves expense data to JSON file."""
        os.makedirs("data", exist_ok=True)
        with open(self.FILE_PATH, "w") as f:
            json.dump(data, f, indent=4)
