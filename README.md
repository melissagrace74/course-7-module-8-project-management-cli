# Python Project Management CLI Tool

Welcome to the **Python Project Management CLI Tool**! This is a simple tool that helps you manage users, projects, and tasks. You can add new users, create projects, and assign tasks to keep everything organized. This tool is great for small projects or teams.

## Features

- **User Management**: You can add new users and link them to projects.
- **Project Management**: Create projects, add descriptions, set due dates, and assign them to users.
- **Task Management**: Add tasks to projects, set their status (like "in-progress"), and assign them to users.

## Prerequisites

Before you start using the tool, you need to make sure you have a few things set up:

1. **Python 3.x**: This tool uses Python 3. You can check if Python is installed on your computer by typing `python --version` in your terminal (or `python3 --version` on macOS/Linux).
2. **Pipenv**: We use Pipenv to manage dependencies (the Python packages we need). To install Pipenv, type this in your terminal:
    ```bash
    pip install pipenv
    ```

## Installation

Follow these steps to get the tool set up on your computer:

1. **Clone the repository** to your computer:
    ```bash
    git clone https://github.com/melissagrace74/course-7-module-8-project-management-cli.git
    cd course-7-module-8-project-management-cli
    ```

2. **Install the project dependencies**:
    This project uses `Pipenv` to manage dependencies. To install them, type:
    ```bash
    pipenv install
    ```

3. **Activate the virtual environment**:
    Pipenv creates a virtual environment to keep everything organized. To activate it, run:
    ```bash
    pipenv shell
    ```

Once you're done, you’re ready to use the tool!

## Usage

After you activate the virtual environment, you can use the following commands to manage users, projects, and tasks.

### 1. Add a User

To add a new user, use this command:
```bash
python main.py add-user --name "Alex" --email "alex@example.com"
