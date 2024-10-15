#!/usr/bin/python3
"""Function that reads a text file and prints to stdout"""


def read_file(filename=""):
    """read and print a file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
