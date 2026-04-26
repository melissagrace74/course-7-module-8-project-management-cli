# models/user.py

class User:
    def __init__(self, name, email, projects=None):
        self.name = name
        self.email = email
        self.projects = projects if projects else []

    def __repr__(self):
        return f"User(name={self.name}, email={self.email})"

    # Convert User instance to a dictionary
    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'projects': [project.to_dict() for project in self.projects]  # Convert projects to dictionaries
        }
    