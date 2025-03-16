class UserManager:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def register_user(self, name):
        user = {"id": self.next_id, "name": name}
        self.users[self.next_id] = user
        self.next_id += 1

    def get_user(self, user_id):
        return self.users.get(user_id, None)

    def view_users(self):
        print("\nRegistered Users:")
        for user in self.users.values():
            print(f"{user['id']}: {user['name']}")
