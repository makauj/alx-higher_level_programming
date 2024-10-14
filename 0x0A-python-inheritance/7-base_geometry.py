#!/usr/bin/python3
"""implementing base geometry"""


class BaseGeometry:
    """new class BaseGeometry"""

    def area(self):
        """raise exception if not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ensure value is validated as an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
