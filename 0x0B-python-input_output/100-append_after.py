#!/usr/bin/python3
"""insert a line of text at a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """search for specific string and append new text"""
    text = ""

    with open(filename, "r") as r:
        for line in r:
            text += line 
            if search_string in line:
                text += new_string

    with open(filename, "w") as w:
        w.write(text)
