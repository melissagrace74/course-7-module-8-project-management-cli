import argparse
import json
from models.user import User
from models.project import Project
from models.task import Task

# Path to the data file
DATA_FILE = "data.json"

# Load users, projects, and tasks from the file
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"users": []}  # Return an empty structure if the file doesn't exist or is empty

# Save users, projects, and tasks to the file
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, default=str, indent=4)

# Store users in memory
users = []

def add_user(args):
    user = User(name=args.name, email=args.email)
    users.append(user)

    # Save the updated users list to the file
    save_data({"users": [user.to_dict() for user in users]})
    print(f"Added user: {user}")

def add_project(args):
    # Find the user by name
    user = next((u for u in users if u.name == args.user), None)
    if not user:
        print(f"User {args.user} not found!")
        return

    project = Project(title=args.title, description=args.description, due_date=args.due_date)
    user.add_project(project)

    # Save the updated users list to the file
    save_data({"users": [user.to_dict() for user in users]})
    print(f"Added project: {project} under user: {user.name}")

def add_task(args):
    project = None
    # Find the project by title
    for user in users:
        project = next((p for p in user.projects if p.title == args.project), None)
        if project:
            break

    if not project:
        print(f"Project {args.project} not found!")
        return

    task = Task(title=args.title, status="pending", assigned_to=args.assigned_to)
    project.add_task(task)

    # Save the updated users list to the file
    save_data({"users": [user.to_dict() for user in users]})
    print(f"Added task: {task} to project: {project.title}")

def main():
    global users
    # Load data from the file at the start
    data = load_data()
    users = [User.from_dict(user_data) for user_data in data["users"]]

    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers()

    # Add user subcommand
    parser_user = subparsers.add_parser('add-user')
    parser_user.add_argument('--name', required=True, help="User's name")
    parser_user.add_argument('--email', required=True, help="User's email")
    parser_user.set_defaults(func=add_user)

    # Add project subcommand
    parser_project = subparsers.add_parser('add-project')
    parser_project.add_argument('--user', required=True, help="User's name to assign the project")
    parser_project.add_argument('--title', required=True, help="Project title")
    parser_project.add_argument('--description', required=True, help="Project description")
    parser_project.add_argument('--due_date', required=True, help="Project due date")
    parser_project.set_defaults(func=add_project)

    # Add task subcommand
    parser_task = subparsers.add_parser('add-task')
    parser_task.add_argument('--project', required=True, help="Project title to assign the task")
    parser_task.add_argument('--title', required=True, help="Task title")
    parser_task.add_argument('--assigned_to', required=True, help="User assigned to the task")
    parser_task.set_defaults(func=add_task)

    # Parse and call the appropriate function
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
    