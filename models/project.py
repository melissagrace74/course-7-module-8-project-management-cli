# models/project.py

class Project:
    def __init__(self, title, description, due_date, tasks=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = tasks if tasks else []

    def __repr__(self):
        return f"Project(title={self.title}, due_date={self.due_date})"

    # Convert Project instance to a dictionary
    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'tasks': [task.to_dict() for task in self.tasks]  # Convert tasks to dictionaries
        }
    