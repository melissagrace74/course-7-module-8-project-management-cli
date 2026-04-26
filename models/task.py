# models/task.py

class Task:
    """
    Represents a Task in the system. Each task has a title, status, and an assigned user.
    """

    def __init__(self, title, status, assigned_to):
        """
        Initializes a Task object with the provided title, status, and assigned user.

        :param title: Title of the task
        :param status: Status of the task (e.g., 'in-progress', 'completed')
        :param assigned_to: User to whom the task is assigned
        """
        self.title = title
        self.status = status
        self.assigned_to = assigned_to

    def to_dict(self):
        """
        Converts the Task object to a dictionary.

        :return: Dictionary representation of the Task object
        """
        return {
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to
        }

    def __repr__(self):
        """
        String representation of the Task object.

        :return: String representation of the Task object
        """
        return f"Task(title={self.title}, status={self.status}, assigned_to={self.assigned_to})"
    