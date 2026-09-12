from datetime import datetime

def validate_task_title(title):
    """Validates that the task title is a non-empty string using len()."""
    if not isinstance(title, str) or len(title) == 0 or len(title.strip()) == 0:
        return False, "Error: Task title cannot be empty."
    return True, ""

def validate_task_description(description):
    """Validates that the task description is a non-empty string using len()."""
    if not isinstance(description, str) or len(description) == 0 or len(description.strip()) == 0:
        return False, "Error: Task description cannot be empty."
    return True, ""

def validate_due_date(due_date):
    """Validates that the due date matches YYYY-MM-DD and explicitly triggers ValueError."""
    if not isinstance(due_date, str):
        return False, "Error: Due date must be a string."
    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True, ""
    except ValueError as e:
        return False, "Error: Due date must be in YYYY-MM-DD format."