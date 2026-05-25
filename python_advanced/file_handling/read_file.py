#!/usr/bin/env python3
"""Module for reading file"""


def read_file(filename=""):
    """read a file"""

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
