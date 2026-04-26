# models/project.py

class Project:
    def __init__(self, title, description, due_date):
        """
        Initializes a new Project object.
        
        Parameters:
        - title (str): The project's title
        - description (str): A brief description of the project
        - due_date (str): The project's due date
        """
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []  # This will hold the list of tasks for the project

    def add_task(self, task):
        """
        Adds a task to the project's list of tasks.
        
        Parameters:
        - task (Task): The task to be added
        """
        self.tasks.append(task)

    def __str__(self):
        return f"Project: {self.title}, Due: {self.due_date}, Tasks: {len(self.tasks)}"

    @classmethod
    def from_dict(cls, data):
        """
        Create a Project instance from a dictionary.
        
        Parameters:
        - data (dict): The dictionary containing project data
        
        Returns:
        - Project: A new Project object
        """
        project = cls(title=data["title"], description=data["description"], due_date=data["due_date"])
        project.tasks = [Task(**task_data) for task_data in data.get("tasks", [])]
        return project

    def to_dict(self):
        """
        Convert the Project instance to a dictionary.
        
        Returns:
        - dict: The dictionary representation of the project
        """
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [task.to_dict() for task in self.tasks]
        }
    