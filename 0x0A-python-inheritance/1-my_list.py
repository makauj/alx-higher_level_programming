#!/usr/bin/python3
"""Defines an inherited list class MyList"""


class MyList(list):
    """MyList class that inherits from list class"""

    def __init__(self):
        """initialize MyList"""
        super().__init__()

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))