# Python Project Management CLI Tool

Welcome to the **Python Project Management CLI Tool**! This is a simple command-line tool to help you manage users, projects, and tasks. You can add new users, create projects, and assign tasks to help keep track of work and progress. This tool is useful for organizing small to medium projects and keeping everyone on track.

## Features

- **User Management**: You can add new users and associate them with projects.
- **Project Management**: Create new projects, give them descriptions, set due dates, and assign them to users.
- **Task Management**: Add tasks to projects, set their status (like "in-progress"), and assign them to users.

## Prerequisites

Before you start, you need to have a few things set up on your computer:

1. **Python 3.x**: Make sure Python 3 is installed on your computer. You can check if Python is installed by typing `python --version` in your terminal (or `python3 --version` on macOS/Linux).
2. **Pipenv**: We use Pipenv to handle Python dependencies (packages). To install Pipenv, you can run:
    ```bash
    pip install pipenv
    ```

## Installation

Follow these steps to get the project running on your computer:

1. **Clone the repository** to your computer:
    ```bash
    git clone https://github.com/melissagrace74/course-7-module-8-project-management-cli.git
    cd course-7-module-8-project-management-cli
    ```

2. **Install the project dependencies**:
    This project uses `Pipenv` to manage its dependencies. You can install them by running:
    ```bash
    pipenv install
    ```

3. **Activate the virtual environment**:
    Pipenv creates a virtual environment to isolate your project dependencies. To activate it, run:
    ```bash
    pipenv shell
    ```

Now your environment is set up and you're ready to start using the tool!

## Usage

Once you're inside the virtual environment, you can run the commands below to manage your users, projects, and tasks.

### 1. Add a User

To add a new user, use the `add-user` command:
```bash
python main.py add-user --name "Alex" --email "alex@example.com"