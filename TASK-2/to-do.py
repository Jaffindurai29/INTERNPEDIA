import os

TODO_FILE = 'tasks.txt'

def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            for line in file:
                task, status = line.strip().split(',')
                tasks.append({"task": task, "done": status == 'True'})
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task['task']},{task['done']}\n")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks to show.")
    else:
        print("\nTo-do List:")
        for idx, task in enumerate(tasks):
            status = "Done" if task['done'] else "Not Done"
            print(f"{idx + 1}. {task['task']} [{status}]")

def add_task(tasks):
    task = input("Enter the new task: ").strip()
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added.")

def mark_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to mark done/undone: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]['done'] = not tasks[task_num]['done']
            status = "done" if tasks[task_num]['done'] else "not done"
            print(f"Task '{tasks[task_num]['task']}' marked as {status}.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input, please enter a valid number.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input, please enter a valid number.")

def show_menu():
    print("\nTo-do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark task as done/undone")
    print("4. Remove a task")
    print("5. Exit")

def main():
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice, please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
