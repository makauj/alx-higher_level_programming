#!/usr/bin/python3
"""function that prints a square with the character #"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")

    square = ""
    for i in range(size):
        square += "#" * size + "\n"
    return square.rstrip()
