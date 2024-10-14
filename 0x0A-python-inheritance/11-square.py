#!/usr/bin/python3
"""Square class that inherits from Rectangle class"""
Rectangle = __import__('9_rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """initialize new square with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    
    def area(self):
        return self.__size ** 2
    
    def __str__(self):
        """Return string representation of a square"""
        return f"[Square] {self.__size}/{self.__size}"