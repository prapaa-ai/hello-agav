"""Read and write a persistent run counter to state.json."""

import json
import os

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), "state.json")


def read_count(path: str = DEFAULT_PATH) -> int:
    """Return the current run count (0 if no state file exists)."""
    if not os.path.exists(path):
        return 0
    with open(path, "r") as f:
        data = json.load(f)
    return data.get("count", 0)


def increment(path: str = DEFAULT_PATH) -> int:
    """Increment the run counter and return the new value."""
    count = read_count(path) + 1
    with open(path, "w") as f:
        json.dump({"count": count}, f)
    return count


def reset(path: str = DEFAULT_PATH) -> None:
    """Reset the counter by removing the state file."""
    if os.path.exists(path):
        os.remove(path)
