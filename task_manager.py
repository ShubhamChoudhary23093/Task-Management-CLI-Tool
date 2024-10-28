import sys
import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the tasks file, returning them as a list of dictionaries."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        tasks = [line.strip().split(", ", 2) for line in file.readlines()]
        return [{"status": status, "name": name, "description": description} for status, name, description in tasks]

def save_tasks(tasks):
    """Save the tasks list to the tasks file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['status']}, {task['name']}, {task['description']}\n")

def add_task(name, description):
    """Add a new task with a name and description to the tasks list."""
    tasks = load_tasks()
    tasks.append({"status": "pending", "name": name, "description": description})
    save_tasks(tasks)
    print(f"Added task: {name} - {description}")

def list_tasks():
    """Display all tasks, grouping them by status (pending and completed)."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return

    def print_task_group(tasks, status):
        print(f"\n{status.capitalize()} Tasks:")
        print("*" * 10)
        for i, task in enumerate(tasks, 1):
            if task["status"] == status:
                print(f"{i}. Task: {task['name']}")
                print(f"   Description: {task['description']}")
                print()

    print_task_group(tasks, "pending")
    print_task_group(tasks, "completed")

def complete_task(task_number):
    """Mark a task as completed based on its task number."""
    tasks = load_tasks()
    if validate_task_number(task_number, tasks):
        task = tasks[task_number - 1]
        if task["status"] == "pending":
            task["status"] = "completed"
            save_tasks(tasks)
            print(f"Completed task: {task['name']} - {task['description']}")
        else:
            print("Task is already completed.")

def delete_task(task_number):
    """Delete a task based on its task number."""
    tasks = load_tasks()
    if validate_task_number(task_number, tasks):
        task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Deleted task: {task['name']} - {task['description']}")

def validate_task_number(task_number, tasks):
    """Check if the given task number is valid for the tasks list."""
    if 1 <= task_number <= len(tasks):
        return True
    print("Invalid task number.")
    return False

def show_usage():
    """Display usage information and command examples for the task manager CLI."""
    print("\nUsage:")
    print("  python task_manager.py <command> [arguments]\n")
    print("Commands:")
    print("  add <name> <description>      Adds a new task with a name and description")
    print("  list                          Displays all tasks, grouped by status (pending/completed)")
    print("  complete <task_number>        Marks a specified task as completed")
    print("  delete <task_number>          Deletes a specified task")
    print("  help                          Displays this help message\n")
    print("Examples:")
    print("  python task_manager.py add 'Buy groceries' 'Get fruits, veggies, and milk'")
    print("  python task_manager.py list")
    print("  python task_manager.py complete 1")
    print("  python task_manager.py delete 2")
    print("\nNote:")
    print("  <task_number> is the task's index in the list as displayed by the 'list' command.")
    print("")

def main():
    """Main function to parse command-line arguments and execute respective task functions."""
    if len(sys.argv) < 2:
        print("Missing command. Type 'python task_manager.py help' to see usage instructions.")
        return

    command = sys.argv[1].lower()
    commands = {
        "add": lambda: add_task(sys.argv[2], sys.argv[3]) if len(sys.argv) == 4 else show_usage(),
        "list": list_tasks,
        "complete": lambda: complete_task(int(sys.argv[2])) if len(sys.argv) == 3 else show_usage(),
        "delete": lambda: delete_task(int(sys.argv[2])) if len(sys.argv) == 3 else show_usage(),
        "help": show_usage
    }

    if command in commands:
        try:
            commands[command]()
        except ValueError:
            print("Error: task number must be an integer.")
    else:
        print("Invalid command. Type 'python task_manager.py help' to see usage instructions.")

if __name__ == "__main__":
    main()
