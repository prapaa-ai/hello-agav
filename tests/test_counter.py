"""Tests for the counter module."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from counter import increment, read_count, reset


def test_read_count_no_file(tmp_path):
    path = str(tmp_path / "state.json")
    assert read_count(path) == 0


def test_increment(tmp_path):
    path = str(tmp_path / "state.json")
    assert increment(path) == 1
    assert increment(path) == 2
    assert increment(path) == 3


def test_read_count_after_increment(tmp_path):
    path = str(tmp_path / "state.json")
    increment(path)
    assert read_count(path) == 1


def test_reset(tmp_path):
    path = str(tmp_path / "state.json")
    increment(path)
    reset(path)
    assert read_count(path) == 0
    assert not os.path.exists(path)
