#!/usr/bin/python3
"""Square"""
Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        self.__size = size
        super().__init__(size, size, x, y, id)