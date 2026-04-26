# utils/file_io.py

import json
from models.user import User
from models.project import Project
from models.task import Task

# Load data from a file
def load_data(file_path, model_class):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return [model_class(**item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save data to a file
def save_data(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump([item.to_dict() for item in data], file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")
        