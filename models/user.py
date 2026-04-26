# models/user.py

from models.project import Project  # <-- Add this import
from models.task import Task  # <-- You may also want to import Task in case it's needed

class User:
    def __init__(self, name, email):
        """
        Initializes a new User object.
        
        Parameters:
        - name (str): The user's name
        - email (str): The user's email address
        """
        self.name = name
        self.email = email
        self.projects = []  # Initialize projects as an empty list

    def add_project(self, project):
        """
        Adds a project to the user's list of projects.
        
        Parameters:
        - project (Project): The project to be added
        """
        self.projects.append(project)

    def __str__(self):
        return f"User: {self.name}, Email: {self.email}, Projects: {len(self.projects)}"

    @classmethod
    def from_dict(cls, data):
        """
        Create a User instance from a dictionary.
        
        Parameters:
        - data (dict): The dictionary containing user data
        
        Returns:
        - User: A new User object
        """
        user = cls(name=data["name"], email=data["email"])
        user.projects = [Project.from_dict(project_data) for project_data in data.get("projects", [])]
        return user

    def to_dict(self):
        """
        Convert the User instance to a dictionary.
        
        Returns:
        - dict: The dictionary representation of the user
        """
        return {
            "name": self.name,
            "email": self.email,
            "projects": [project.to_dict() for project in self.projects]
        }
    