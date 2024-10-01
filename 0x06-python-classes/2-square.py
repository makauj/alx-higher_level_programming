#!/usr/bin/python3
"""Empty class to define Square"""


class Square:
    """Empty class(Does nothing)"""

    def __init__(self, size="0"):
        """init this square class with argumnet `size`"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
