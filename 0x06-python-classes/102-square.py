#!/usr/bin/python3
"""Empty class to define Square"""


class Square:
    """Empty class(Does nothing)"""

    def __init__(self, size=0):
        """init this square class with argumnet `size`"""

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ne__(self, other):
        return self.area() != other.area()
