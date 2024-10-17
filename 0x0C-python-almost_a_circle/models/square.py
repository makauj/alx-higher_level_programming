#!/usr/bin/python3
"""Square"""
Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize a square"""
        super().__init__(size, size, x, y, id)

    # getters for a square
    @property
    def size(self):
        """get size"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """set value for size"""
        self.width = value
        self.height = value
