import argparse
from models.user import User
from models.project import Project
from models.task import Task
from utils.file_io import load_data, save_data

# Load initial data
users = load_data('data/users.json', User)
projects = load_data('data/projects.json', Project)
tasks = load_data('data/tasks.json', Task)

def add_user(name, email):
    """Adds a user and saves to file."""
    user = User(name, email)
    users.append(user)
    save_data('data/users.json', users)
    print(f"User {name} added.")

def add_project(user_name, title, description, due_date):
    """Adds a project to a user and saves to file."""
    user = next((u for u in users if u.name == user_name), None)
    if user:
        project = Project(title, description, due_date)
        user.add_project(project)
        save_data('data/users.json', users)
        save_data('data/projects.json', projects)  # Also save projects
        print(f"Project '{title}' added to {user_name}.")
    else:
        print(f"User '{user_name}' not found.")

def add_task(project_title, task_title):
    """Adds a task to a project and saves to file."""
    project = next((p for p in projects if p.title == project_title), None)
    if project:
        task = Task(task_title)
        project.add_task(task)
        save_data('data/projects.json', projects)
        save_data('data/tasks.json', tasks)  # Save tasks as well
        print(f"Task '{task_title}' added to project '{project_title}'.")
    else:
        print(f"Project '{project_title}' not found.")

def complete_task(project_title, task_title):
    """Marks a task as completed and saves to file."""
    for project in projects:
        if project.title == project_title:
            task = next((t for t in project.tasks if t.title == task_title), None)
            if task:
                task.status = "Completed"
                save_data('data/projects.json', projects)
                print(f"Task '{task_title}' in project '{project_title}' marked as completed.")
                return
    print(f"Task '{task_title}' not found in project '{project_title}'.")

def main():
    parser = argparse.ArgumentParser(description="CLI Tool for Project Management")
    subparsers = parser.add_subparsers()

    # Add user
    user_parser = subparsers.add_parser('add-user', help="Add a new user")
    user_parser.add_argument('--name', type=str, required=True, help="Name of the user")
    user_parser.add_argument('--email', type=str, required=True, help="Email of the user")
    user_parser.set_defaults(func=lambda args: add_user(args.name, args.email))

    # Add project
    project_parser = subparsers.add_parser('add-project', help="Add a new project to a user")
    project_parser.add_argument('--user', type=str, required=True, help="User to assign the project to")
    project_parser.add_argument('--title', type=str, required=True, help="Title of the project")
    project_parser.add_argument('--description', type=str, required=True, help="Description of the project")
    project_parser.add_argument('--due-date', type=str, required=True, help="Due date of the project")
    project_parser.set_defaults(func=lambda args: add_project(args.user, args.title, args.description, args.due_date))

    # Add task
    task_parser = subparsers.add_parser('add-task', help="Add a new task to a project")
    task_parser.add_argument('--project', type=str, required=True, help="Project to add the task to")
    task_parser.add_argument('--title', type=str, required=True, help="Title of the task")
    task_parser.set_defaults(func=lambda args: add_task(args.project, args.title))

    # Complete task
    complete_parser = subparsers.add_parser('complete-task', help="Mark a task as completed")
    complete_parser.add_argument('--project', type=str, required=True, help="Project containing the task")
    complete_parser.add_argument('--title', type=str, required=True, help="Title of the task")
    complete_parser.set_defaults(func=lambda args: complete_task(args.project, args.title))

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
    