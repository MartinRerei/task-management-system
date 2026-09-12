from datetime import datetime

def validate_task_title(title):
    """Checks if the title is not empty."""
    if not isinstance(title, str) or len(title.strip()) == 0:
        return False, "Error: Task title cannot be empty."
    return True, ""

def validate_task_description(description):
    """Checks if the description is not empty."""
    if not isinstance(description, str) or len(description.strip()) == 0:
        return False, "Error: Task description cannot be empty."
    return True, ""

def validate_due_date(due_date):
    """Checks if the date matches the YYYY-MM-DD format."""
    if not isinstance(due_date, str):
        return False, "Error: Due date must be a string."
    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True, ""
    except ValueError:
        return False, "Error: Due date must be in YYYY-MM-DD format."