
# Task 13: To-Do List Manager

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            print("Could not read saved tasks. Starting with an empty list.")
    return []


def save_tasks(tasks):
    DATA_FILE.write_text(
        json.dumps(tasks, indent=4),
        encoding="utf-8"
    )


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
        return

    print("\nYOUR TASKS")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. [{status}] {task['title']}")


def main():
    tasks = load_tasks()

    while True:
        print("\n" + "=" * 35)
        print("TO-DO LIST MANAGER")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task completed")
        print("4. Delete task")
        print("5. Exit")
        print("=" * 35)

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            title = input("Enter task: ").strip()
            if title:
                tasks.append({"title": title, "completed": False})
                save_tasks(tasks)
                print("Task added.")
            else:
                print("Task cannot be empty.")

        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                try:
                    number = int(input("Task number to complete: "))
                    if 1 <= number <= len(tasks):
                        tasks[number - 1]["completed"] = True
                        save_tasks(tasks)
                        print("Task marked completed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Enter a valid number.")

        elif choice == "4":
            show_tasks(tasks)
            if tasks:
                try:
                    number = int(input("Task number to delete: "))
                    if 1 <= number <= len(tasks):
                        removed = tasks.pop(number - 1)
                        save_tasks(tasks)
                        print(f"Deleted: {removed['title']}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Enter a valid number.")

        elif choice == "5":
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
