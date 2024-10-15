#!/usr/bin/python3
"""insert a line of text at a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """search for specific string and append new text"""
    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "a") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
