from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)

def main():
    tasks = []
    
    while True:
        print("\n--- Task Management System ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. Track Progress")
        print("5. Exit")
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
        except EOFError:
            break
            
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            
            success, message = add_task(tasks, title, description, due_date)
            print(message)
            
        elif choice == "2":
            title = input("Enter task title or number: ")
            success, message = mark_task_as_complete(tasks, title)
            print(message)
            
        elif choice == "3":
            pending = view_pending_tasks(tasks)
            if not pending:
                print("No pending tasks found.")
            else:
                print("\n--- Pending Tasks ---")
                for idx, task in enumerate(pending, 1):
                    print(f"{idx}. {task['title']} - {task['description']} (Due: {task['due_date']})")
                    
        elif choice == "4":
            progress = calculate_progress(tasks)
            print(f"Current Progress: {progress}% completed.")
            
        elif choice == "5":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid number from 1 to 5.")

if __name__ == "__main__":
    main()