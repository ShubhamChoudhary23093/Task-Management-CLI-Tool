# Task Manager CLI

A command-line interface (CLI) for managing tasks. This application allows you to add, list, mark as complete, and delete tasks, all from the terminal. Tasks are stored in a text file (`tasks.txt`) and grouped by their status (pending and completed).

## Features

- **Add a Task:** Add a task with a name and description.
- **List Tasks:** View all tasks grouped by their current status.
- **Complete a Task:** Mark a specified task as completed.
- **Delete a Task:** Remove a specified task from the list.

## Requirements

- Python 3.x

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>


## Usage

| Command                   | Description                                          |
|---------------------------|------------------------------------------------------|
| `add <name> <description>` | Adds a new task with the specified name and description. |
| `list`                    | Lists all tasks, grouped by their status.            |
| `complete <task_number>`  | Marks the task with the given number as completed.   |
| `delete <task_number>`    | Deletes the task with the specified task number.     |
| `help`                    | Displays usage information and command examples.     |


### Examples

- **To add a task:**
   ```bash
   python task_manager.py add "Buy groceries" "Get fruits, veggies, and milk"

- **To Complete a task:**
   ```bash
   python task_manager.py complete <task_number>

- **To list all taks:**
   ```bash
   python task_manager.py list

- **To delete a task:**
   ```bash
   python task_manager.py delete <task_number>

- **To check for Help:**
   ```bash
   python task_manager.py help

Output Explanation
When you use the list command, tasks are displayed in the following format:

Output - pending, Groceries, Oil, Vegetables, Rice

The output columns mean the following:

First Column (Status): The current status of the task, either pending or completed.

Second Column (Task Name): The main task or objective that needs to be completed.

Remaining Columns (Description): Additional details or a breakdown of the task, describing specific items or subtasks required for completion.

