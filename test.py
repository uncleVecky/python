#Create a simple to-do list program that allows the user to:
#Add tasks
#View all tasks
#Mark tasks as complete
#Remove tasks

def main():
    while True:
        print("1. Add task")
        print("2. View all tasks")
        print("3. Mark task as complete")
        print("4. Remove task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_as_complete()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")  

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully.")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def mark_task_as_complete():
    view_tasks()
    task_index = int(input("Enter the task number to mark as complete: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number. Please try again.")
    else:
        tasks[task_index] = "[X] " + tasks[task_index]
        print("Task marked as complete.")

def remove_task():
    view_tasks()
    task_index = int(input("Enter the task number to remove: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number. Please try again.")
    else:
        del tasks[task_index]
        print("Task removed successfully.")

tasks = []
main() 