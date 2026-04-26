# utils/file_io.py
import json
import os

def load_data(file_path, model_class=None):
    """Loads data from a JSON file and converts it to objects."""
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            if model_class:
                return [model_class(**item) for item in data]
            return data
        except json.JSONDecodeError:
            return []

def save_data(file_path, data):
    """Saves a list of objects to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump([item.to_dict() for item in data], file, indent=4)
        