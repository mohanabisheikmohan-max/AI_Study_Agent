from datetime import date

def calculator(expression: str) -> str:
    """Calculate a basic arithmetic expression."""
    allowed = set("0123456789+-*/(). %")
    if not expression or any(ch not in allowed for ch in expression):
        return "Invalid arithmetic expression."
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception:
        return "Could not calculate the expression."

def current_date() -> str:
    """Return today's date."""
    return date.today().isoformat()
