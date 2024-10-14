#!/usr/bin/python3
"""Defines an inherited list class MyList"""


class MyList(list):
    """MyList class that inherits from list class"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        sorted_list = self[:]

        for i in range(len(sorted_list)):
            for j in range(0, len(sorted_list) - i - 1):
                if sorted_list[j] > sorted_list[j + 1]:
                    sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
        print(sorted_list)