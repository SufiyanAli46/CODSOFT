class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task has been added: {task}")

    def view_tasks(self):
        print("To-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task has been removed: {removed_task}")
        else:
            print("Invalid task number.")

# Create a To-Do List instance
todo_list = ToDoList()

# User interface loop
while True:
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter the task you want to add: ")
        todo_list.add_task(task)
    elif choice == '2':
        todo_list.view_tasks()
    elif choice == '3':
        task_number = int(input("Enter the task number to remove: "))
        todo_list.remove_task(task_number)
    elif choice == '4':
        print("Exiting the To-Do List Application.")
        break
    else:
        print("Invalid option. Please try again boss.")