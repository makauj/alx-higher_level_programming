#!/usr/bin/python3
"""function that checks if obj is exactly an instance of a_class"""


def is_same_class(obj, a_class):
    """function code"""
    if type(obj) is a_class:
        return True
    else:
        return False
