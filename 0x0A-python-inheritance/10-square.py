#!/usr/bin/python3
"""Square class that inherits from Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """new class Square"""

    def __init__(self, size):
        """initialize Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
