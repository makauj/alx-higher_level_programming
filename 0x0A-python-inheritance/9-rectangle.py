#!/usr/bin/python3
"""A class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """
        Initialize a new rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of a rectangle"""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
