import os

TASKS_FILE = "tasks.txt"

def load_tasks():

    """Load tasks from the text file into a list."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]
        
def save_tasks(tasks):

    """Save tasks from the list to the text file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")
            
def view_tasks(tasks):

    """Display all tasks."""
    if not tasks:
        print("\nNo tasks found.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()
        
def add_task(tasks):

    """Add a new task to the list."""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Task cannot be empty.")
        
def remove_task(tasks):

    """Remove a task by its number."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
        
def main():

    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")
            
if __name__ == "__main__":
    main()