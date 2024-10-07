#!/usr/bin/python3
"""Class to define Rectangle
include private instance attributes width and height
"""


class Rectangle:
    """instantiate width and height"""
    def __init__(self, width=0, height=0):

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise TypeError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise TypeError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
