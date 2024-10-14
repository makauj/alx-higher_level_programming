#!/usr/bin/python3
"""function that checks if obj is an instance of an inherited class"""


def is_kind_of_class(obj, a_class):
    """
    if object is an instance of an inherited class,
    return True else False
    """
    return isinstance(obj, a_class)
