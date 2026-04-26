class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.projects = []  # List to hold projects assigned to the user

    def __str__(self):
        return f"User {self.name} ({self.email})"