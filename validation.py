from datetime import datetime

def validate_task_title(title):
    """Validates that the task title is a non-empty string using len()."""
    if len(title.strip()) == 0:
        raise ValueError("Error: Task title cannot be empty.")
    return True

def validate_task_description(description):
    """Validates that the task description is a non-empty string using len()."""
    if len(description.strip()) == 0:
        raise ValueError("Error: Task description cannot be empty.")
    return True

def validate_due_date(due_date):
    """Validates that the due date matches YYYY-MM-DD and checks for ValueError."""
    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
    except ValueError:
        raise ValueError("Error: Due date must be in YYYY-MM-DD format.")
    return True