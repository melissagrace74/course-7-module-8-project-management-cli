# main.py

import argparse
from models.user import User
from models.project import Project
from models.task import Task
from utils.file_io import load_data, save_data

# Load users, projects, and tasks
users = load_data('data/users.json', User)
projects = load_data('data/projects.json', Project)
tasks = load_data('data/tasks.json', Task)

# Helper functions to add data
def add_user(name, email):
    user = User(name, email)
    users.append(user)
    save_data('data/users.json', users)
    print(f"User {name} added.")

def add_project(user_name, title, description, due_date):
    user = next((u for u in users if u.name == user_name), None)
    if user:
        project = Project(title, description, due_date)
        user.projects.append(project)
        save_data('data/users.json', users)  # Save updated user with projects
        print(f"Project '{title}' added to {user_name}.")
    else:
        print(f"User {user_name} not found.")

def add_task(project_title, title, status, assigned_to):
    project = next((p for p in projects if p.title == project_title), None)
    if project:
        task = Task(title, status, assigned_to)
        project.tasks.append(task)
        save_data('data/projects.json', projects)  # Save updated projects with tasks
        print(f"Task '{title}' added to project '{project_title}'.")
    else:
        print(f"Project '{project_title}' not found.")

# Setup CLI parser
def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers()

    # Add User
    user_parser = subparsers.add_parser('add-user', help='Add a new user')
    user_parser.add_argument('--name', required=True, help="Name of the user")
    user_parser.add_argument('--email', required=True, help="Email of the user")
    user_parser.set_defaults(func=lambda args: add_user(args.name, args.email))

    # Add Project
    project_parser = subparsers.add_parser('add-project', help='Add a project to a user')
    project_parser.add_argument('--user', required=True, help="User name")
    project_parser.add_argument('--title', required=True, help="Project title")
    project_parser.add_argument('--description', required=True, help="Project description")
    project_parser.add_argument('--due-date', required=True, help="Due date for the project")
    project_parser.set_defaults(func=lambda args: add_project(args.user, args.title, args.description, args.due_date))

    # Add Task
    task_parser = subparsers.add_parser('add-task', help='Add a task to a project')
    task_parser.add_argument('--project', required=True, help="Project title")
    task_parser.add_argument('--title', required=True, help="Task title")
    task_parser.add_argument('--status', required=True, help="Task status")
    task_parser.add_argument('--assigned-to', required=True, help="Assigned user")
    task_parser.set_defaults(func=lambda args: add_task(args.project, args.title, args.status, args.assigned_to))

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
    