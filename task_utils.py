from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

def add_task(tasks_list, title, description, due_date):
    """Validates input using ValueError and adds a new task to the list."""
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
    except ValueError as e:
        return False, str(e)
        
    new_task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False
    }
    tasks_list.append(new_task)
    return True, "Task added successfully!"

def mark_task_as_complete(tasks_list, identifier):
    """Marks a task as complete based on its title or its list index."""
    for i, task in enumerate(tasks_list, 1):
        # Checks if the user typed the title OR the task number (like '1')
        if task["title"].lower() == identifier.strip().lower() or str(i) == identifier.strip():
            if task["completed"]:
                return False, "Task is already completed."
            task["completed"] = True
            return True, "Task marked as complete!"
    return False, "Error: Task not found."

def view_pending_tasks(tasks_list):
    """Returns a list of tasks that have not been completed yet."""
    return [task for task in tasks_list if not task["completed"]]

def calculate_progress(tasks_list):
    """Calculates the percentage of completed tasks."""
    if not tasks_list:
        return 0.0
    completed_count = sum(1 for task in tasks_list if task["completed"])
    return round((completed_count / len(tasks_list)) * 100, 2)