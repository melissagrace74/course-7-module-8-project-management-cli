class Project:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []  # List to hold tasks assigned to the project

    def __str__(self):
        return f"Project {self.title} - Due: {self.due_date}"
    