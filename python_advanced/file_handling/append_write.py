#!/usr/bin/env python3
"""Module for append a file"""


def append_write(filename="", text=""):
    """append a file"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
