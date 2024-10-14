#!/usr/bin/python3
"""function that adds attributes to objects"""


def add_attribute(obj, attribute, value):
    """
    add new attribute to an object, raise exception if not possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
