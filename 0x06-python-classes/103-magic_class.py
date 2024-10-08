#!/usr/bin/python3
"""Writing a doctring"""
import math


class MagicClass:
    """Initialize the MagicClass with a given radius."""

    def __init__(self, radius=0):
        self.radius = 0

        if type(radius) is not int and type(radius is not float):
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Return area of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """return circumference of the circle"""
        return 2 * self.__radius * math.pi
