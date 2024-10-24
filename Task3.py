def show_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")


def todoList():
    tasks = []
    while True:
        print("\n1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            task = input("Enter a new task: ")
            tasks.append(task)
        elif choice == '3':
            show_tasks(tasks)
            task_num = int(input("Enter task number to remove: "))
            if 0 < task_num <= len(tasks):
                tasks.pop(task_num - 1)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    todoList()
