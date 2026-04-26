# models/task.py

class Task:
    def __init__(self, title, status, assigned_to):
        """
        Initializes a new Task object.
        
        Parameters:
        - title (str): The task's title
        - status (str): The task's status, e.g., 'pending' or 'completed'
        - assigned_to (str): The user assigned to this task
        """
        self.title = title
        self.status = status
        self.assigned_to = assigned_to

    def mark_complete(self):
        """Marks the task as complete."""
        self.status = "completed"

    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}, Assigned to: {self.assigned_to}"

    @classmethod
    def from_dict(cls, data):
        """
        Create a Task instance from a dictionary.
        
        Parameters:
        - data (dict): The dictionary containing task data
        
        Returns:
        - Task: A new Task object
        """
        return cls(title=data["title"], status=data["status"], assigned_to=data["assigned_to"])

    def to_dict(self):
        """
        Convert the Task instance to a dictionary.
        
        Returns:
        - dict: The dictionary representation of the task
        """
        return {
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to
        }
    