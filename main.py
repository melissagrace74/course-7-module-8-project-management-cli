# main.py

import argparse
from models.user import User
from models.project import Project
from models.task import Task
from utils.file_io import load_data, save_data

# Load users data from JSON
users = load_data('data/users.json', User)

def add_user(name, email):
    """Add a new user."""
    user = User(name, email)
    users.append(user)
    save_data('data/users.json', users)
    print(f"User {name} added.")

def add_project(user_name, title, description, due_date):
    """Add a new project to a user."""
    user = next((u for u in users if u.name == user_name), None)
    if user:
        project = Project(title, description, due_date)
        user.projects.append(project)
        save_data('data/users.json', users)
        print(f"Project '{title}' added to {user_name}.")
    else:
        print(f"User {user_name} not found.")

def add_task(project_title, title, status, assigned_to):
    """Add a task to a project."""
    user = next((u for u in users if any(p.title == project_title for p in u.projects)), None)
    if user:
        project = next(p for p in user.projects if p.title == project_title)
        task = Task(title, status, assigned_to)
        project.tasks.append(task)
        save_data('data/users.json', users)
        print(f"Task '{title}' added to project '{project_title}'.")
    else:
        print(f"Project {project_title} not found.")

# Setting up argparse for CLI commands
def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers(help="sub-command help")

    # Add user
    user_parser = subparsers.add_parser('add-user', help="Add a new user")
    user_parser.add_argument('--name', required=True, help="User's name")
    user_parser.add_argument('--email', required=True, help="User's email")
    user_parser.set_defaults(func=lambda args: add_user(args.name, args.email))

    # Add project
    project_parser = subparsers.add_parser('add-project', help="Add a new project")
    project_parser.add_argument('--user', required=True, help="User's name to add the project to")
    project_parser.add_argument('--title', required=True, help="Project title")
    project_parser.add_argument('--description', required=True, help="Project description")
    project_parser.add_argument('--due-date', required=True, help="Project due date")
    project_parser.set_defaults(func=lambda args: add_project(args.user, args.title, args.description, args.due_date))

    # Add task
    task_parser = subparsers.add_parser('add-task', help="Add a new task to a project")
    task_parser.add_argument('--project', required=True, help="Project title to add the task to")
    task_parser.add_argument('--title', required=True, help="Task title")
    task_parser.add_argument('--status', required=True, choices=['in-progress', 'completed'], help="Task status")
    task_parser.add_argument('--assigned-to', required=True, help="User assigned to the task")
    task_parser.set_defaults(func=lambda args: add_task(args.project, args.title, args.status, args.assigned_to))

    # Parse the arguments and call the appropriate function
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
    