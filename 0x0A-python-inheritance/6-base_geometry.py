#!/usr/bin/python3
"""class BaseGeometry that raises an Exception"""


class BaseGeometry:
    """class only raises and exception"""

    def area(self):
        """area raises exception if not implemented"""
        raise Exception("area() is not implemented")
