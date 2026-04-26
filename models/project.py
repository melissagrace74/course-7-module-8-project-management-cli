# models/project.py

class Project:
    """
    Represents a Project in the system. Each project has a title, description, due date, and optional tasks.
    """

    def __init__(self, title, description, due_date, tasks=None):
        """
        Initializes a Project object with the provided title, description, due date, and optional tasks.

        :param title: Title of the project
        :param description: Description of the project
        :param due_date: Due date of the project
        :param tasks: List of Task objects associated with the project (default is an empty list)
        """
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = tasks or []  # Initialize tasks as an empty list if not provided

    def to_dict(self):
        """
        Converts the Project object to a dictionary, including task data.

        :return: Dictionary representation of the Project object
        """
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [task.to_dict() for task in self.tasks]  # Assuming Task has a to_dict method
        }

    def __repr__(self):
        """
        String representation of the Project object.

        :return: String representation of the Project object
        """
        return f"Project(title={self.title}, description={self.description}, due_date={self.due_date}, tasks={self.tasks})"
    