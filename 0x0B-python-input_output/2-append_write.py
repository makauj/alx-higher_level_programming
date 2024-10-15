#!/usr/bin/python3
"""function to open a file and print its contents"""


def append_write(filename="", text=""):
    """Write a string to a UTF* text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
