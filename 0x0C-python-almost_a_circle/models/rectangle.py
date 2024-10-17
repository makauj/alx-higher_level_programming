#!/usr/bin/python3
"""new Rectangle class"""
Base = __import__('base').Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize rectangle"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
    
    @property
    def width(self):
        """get value of width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """set value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        """get value of height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """set value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def x(self):
        """get value of x"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """set value for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get value of y"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """"set value of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of rectangle"""
        return self.__height * self.__width
    
    def display(self):
        """print rectangle using #"""
        for _ in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()
    
    def __str__(self):
        """
        define the format of the string representation of a rectange
        """
        return (f"[Rectangle] ({self.__id})
                {self.__x} / {self.__y} - {self.__width}/{self.__height}")
    
    def update(self, *args):
        """public method to assign an arg to each attribute"""
        if len(args) >= 1:
            self.id >= args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
