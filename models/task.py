# models/task.py

class Task:
    def __init__(self, title, status, assigned_to=None):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to

    def __repr__(self):
        return f"Task(title={self.title}, status={self.status}, assigned_to={self.assigned_to})"

    # Convert Task instance to a dictionary
    def to_dict(self):
        return {
            'title': self.title,
            'status': self.status,
            'assigned_to': self.assigned_to
        }
    