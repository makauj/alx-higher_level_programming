#!/usr/bin/python3
"""base class"""


class Base:
    """Base class"""

    __nb_objects = 0
    def __init__(self, id=None):
        """initialize Base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
