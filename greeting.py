"""Build a greeting string with the user's name and run count."""

from datetime import datetime


def build_greeting(name: str, count: int, now: datetime | None = None) -> str:
    """Return a personalised greeting string.

    Parameters
    ----------
    name:  The user's name.
    count: How many times the CLI has been run.
    now:   Optional datetime override (for testing).
    """
    if now is None:
        now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    runs = "time" if count == 1 else "times"
    return f"Hello, {name}! You have run this {count} {runs}. ({timestamp})"
