"""Tests for the greeting module."""

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from greeting import build_greeting


def test_greeting_with_name():
    now = datetime(2025, 1, 15, 10, 30, 0)
    result = build_greeting("Alice", 3, now=now)
    assert result == "Hello, Alice! You have run this 3 times. (2025-01-15 10:30:00)"


def test_greeting_singular():
    now = datetime(2025, 6, 1, 8, 0, 0)
    result = build_greeting("Bob", 1, now=now)
    assert "1 time." in result
    assert "1 times" not in result


def test_greeting_default_name():
    now = datetime(2025, 3, 20, 14, 45, 0)
    result = build_greeting("World", 5, now=now)
    assert result.startswith("Hello, World!")
