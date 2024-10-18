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

    def update(self, *args, **kwargs):
        """public method that assignes attributes"""
        if args in len(kwargs):
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
                        self.__init__(self.sie, self.x, self.y)
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
