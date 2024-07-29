import os

# Define the filename where tasks will be saved
FILENAME = 'tasks.txt'

# Load tasks from the file
def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            tasks = [line.strip() for line in file]
    return tasks

# Save tasks to the file
def save_tasks(tasks):
    with open(FILENAME, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Add a task to the list
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

# View all tasks in the list
def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Delete a task from the list
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main function to run the application
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()