# models/user.py
class User:
    def __init__(self, name, email, projects=None):
        """Initialize a user with a name, email, and an optional list of projects."""
        self.name = name
        self.email = email
        self.projects = projects if projects is not None else []

    def add_project(self, project):
        """Adds a project to the user's list of projects."""
        self.projects.append(project)

    def to_dict(self):
        """Convert the User object to a dictionary."""
        return {
            "name": self.name,
            "email": self.email,
            "projects": [project.to_dict() for project in self.projects]  # Convert projects to dicts
        }

    def __repr__(self):
        """String representation of a User."""
        return f"User(name={self.name}, email={self.email}, projects={self.projects})"
    