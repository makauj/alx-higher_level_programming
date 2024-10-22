#!/usr/bin/python3
"""Square"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize a square"""
        super().__init__(size, size, x, y, id)

    # getters for a square
    @property
    def size(self):
        """get size"""
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """set value for size"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        self.width = value
        self.height = value

    def __str__(self):
        """str method for square"""
        return (f"[Square] ({self.id}) \
                {self.x}/{self.y} - {self.size}/{self.size}")

    def update(self, *args, **kwargs):
        """public method that assigns attributes"""
        if args:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """method that returns a dictionary with properties"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
