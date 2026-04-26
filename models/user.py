# models/user.py

class User:
    """
    Represents a User in the system. Each user has a name, email, and a list of associated projects.
    """

    def __init__(self, name, email, projects=None):
        """
        Initializes a User object with the provided name, email, and optional projects.

        :param name: Name of the user
        :param email: Email of the user
        :param projects: List of Project objects associated with the user (default is an empty list)
        """
        self.name = name
        self.email = email
        self.projects = projects or []  # Default to empty list if no projects are provided

    def to_dict(self):
        """
        Converts the User object to a dictionary, including project data.

        :return: Dictionary representation of the User object
        """
        return {
            "name": self.name,
            "email": self.email,
            "projects": [project.to_dict() for project in self.projects],  # Serialize each project
        }

    def __repr__(self):
        """
        String representation of the User object.

        :return: String representation of the User object
        """
        return f"User(name={self.name}, email={self.email}, projects={self.projects})"
    