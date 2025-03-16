def format_title(title):
    """Formats book titles to follow proper case."""
    return title.title()

def format_username(name):
    """Capitalizes user names correctly."""
    return name.strip().title()

def format_transaction(action):
    """Formats transaction types for consistency."""
    if action.lower() in ["borrow", "return"]:
        return action.lower()
    return "unknown"

def format_currency(amount):
    """Formats numbers as currency (used for fine calculations)."""
    return f"${amount:,.2f}"
