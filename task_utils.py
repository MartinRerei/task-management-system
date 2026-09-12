from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

def add_task(tasks_list, title, description, due_date):
    """Validates input and adds a new task dictionary to the list."""
    valid_title, title_msg = validate_task_title(title)
    if not valid_title:
        return False, title_msg
        
    valid_desc, desc_msg = validate_task_description(description)
    if not valid_desc:
        return False, desc_msg
        
    valid_date, date_msg = validate_due_date(due_date)
    if not valid_date:
        return False, date_msg
        
    new_task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False
    }
    tasks_list.append(new_task)
    return True, "Task added successfully."

def mark_task_as_complete(tasks_list, title):
    """Marks an existing task as complete based on its title."""
    for task in tasks_list:
        if task["title"].lower() == title.strip().lower():
            if task["completed"]:
                return False, "Task is already completed."
            task["completed"] = True
            return True, "Task marked as complete."
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