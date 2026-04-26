# models/task.py
class Task:
    def __init__(self, title, status, assigned_to=None):
        """Initialize a task with a title, status, and optional assigned user."""
        self.title = title
        self.status = status
        self.assigned_to = assigned_to

    def to_dict(self):
        """Convert the Task object to a dictionary."""
        return {
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to
        }

    def __repr__(self):
        """String representation of the Task."""
        return f"Task(title={self.title}, status={self.status}, assigned_to={self.assigned_to})"
    