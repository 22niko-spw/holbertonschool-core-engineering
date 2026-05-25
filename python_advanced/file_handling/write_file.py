#!/usr/bin/env python3
"""Module for write a file"""


def write_file(filename="", text=""):
    """write a file"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
