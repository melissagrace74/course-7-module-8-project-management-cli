import argparse
from rich.console import Console
from rich.text import Text
from models.user import User
from models.project import Project
from models.task import Task
from utils.file_io import load_data, save_data

# Initialize rich console
console = Console()

# Load user data
def add_user(name, email):
    try:
        users = load_data('data/users.json', User)
        user = User(name, email)
        users.append(user)
        save_data('data/users.json', users)
        console.print(f"[green]User {name} added successfully![/green]")
    except Exception as e:
        console.print(f"[red]Error adding user: {e}[/red]")

# Add project to user
def add_project(user_name, title, description, due_date):
    try:
        users = load_data('data/users.json', User)
        user = next((u for u in users if u.name == user_name), None)
        if user is None:
            console.print(f"[red]User {user_name} not found![/red]")
            return
        project = Project(title, description, due_date)
        user.projects.append(project)
        save_data('data/users.json', users)
        console.print(f"[blue]Project '{title}' added to {user_name}.[/blue]")
    except Exception as e:
        console.print(f"[red]Error adding project: {e}[/red]")

# Add task to project
def add_task(project_title, task_title, status, assigned_to):
    try:
        users = load_data('data/users.json', User)
        user = next((u for u in users if any(p.title == project_title for p in u.projects)), None)
        if user is None:
            console.print(f"[red]Project {project_title} not found![/red]")
            return
        project = next(p for p in user.projects if p.title == project_title)
        task = Task(task_title, status, assigned_to)
        project.tasks.append(task)
        save_data('data/users.json', users)
        console.print(f"[yellow]Task '{task_title}' added to project '{project_title}'[/yellow]")
    except Exception as e:
        console.print(f"[red]Error adding task: {e}[/red]")

# Main function to parse commands
def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers()

    # Add user command
    user_parser = subparsers.add_parser('add-user', help="Add a new user")
    user_parser.add_argument('--name', required=True, help="User's name")
    user_parser.add_argument('--email', required=True, help="User's email")
    user_parser.set_defaults(func=lambda args: add_user(args.name, args.email))

    # Add project command
    project_parser = subparsers.add_parser('add-project', help="Add a new project to a user")
    project_parser.add_argument('--user', required=True, help="User's name")
    project_parser.add_argument('--title', required=True, help="Project title")
    project_parser.add_argument('--description', required=True, help="Project description")
    project_parser.add_argument('--due-date', required=True, help="Project due date")
    project_parser.set_defaults(func=lambda args: add_project(args.user, args.title, args.description, args.due_date))

    # Add task command
    task_parser = subparsers.add_parser('add-task', help="Add a new task to a project")
    task_parser.add_argument('--project', required=True, help="Project title")
    task_parser.add_argument('--title', required=True, help="Task title")
    task_parser.add_argument('--status', required=True, help="Task status")
    task_parser.add_argument('--assigned-to', required=True, help="Task assigned user")
    task_parser.set_defaults(func=lambda args: add_task(args.project, args.title, args.status, args.assigned_to))

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
    