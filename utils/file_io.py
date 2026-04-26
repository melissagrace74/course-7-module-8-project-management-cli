# utils/file_io.py

import json
from models.user import User
from models.project import Project
from models.task import Task  # Import Task class

def load_data(filename, model_class):
    """
    Loads data from a JSON file and converts it into a list of model instances.

    :param filename: The path to the JSON file
    :param model_class: The class to which the data should be converted (User, Project, etc.)
    :return: A list of model instances
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)

        # Convert the data into model instances
        if model_class == User:
            # For Users, we need to initialize projects and tasks
            return [
                User(
                    item['name'],
                    item['email'],
                    [
                        Project(
                            project['title'],
                            project['description'],
                            project['due_date'],
                            [Task(**task) for task in project.get('tasks', [])]  # Handle tasks if they exist
                        ) for project in item['projects']
                    ]
                ) for item in data
            ]
        else:
            # For other models, just return the direct mapping
            return [model_class(**item) for item in data]
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return []
    except json.JSONDecodeError:
        # If there's an error in decoding the JSON, return an empty list
        return []

def save_data(filename, data):
    """
    Saves a list of model instances to a JSON file.

    :param filename: The path to the JSON file
    :param data: The list of model instances to save
    """
    try:
        with open(filename, 'w') as file:
            # Convert model instances to dictionaries before saving
            json.dump([item.to_dict() for item in data], file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")
        