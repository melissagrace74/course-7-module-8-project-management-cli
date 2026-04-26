# models/project.py
class Project:
    def __init__(self, title, description, due_date, tasks=None):
        """Initialize a project with a title, description, due date, and optional tasks."""
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = tasks if tasks is not None else []

    def add_task(self, task):
        """Add a task to the project's task list."""
        self.tasks.append(task)

    def to_dict(self):
        """Convert the Project object to a dictionary."""
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [task.to_dict() for task in self.tasks]  # Convert tasks to dicts
        }

    def __repr__(self):
        """String representation of the Project."""
        return f"Project(title={self.title}, description={self.description}, due_date={self.due_date})"
    