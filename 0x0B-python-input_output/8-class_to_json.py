#!/usr/bin/python3
"""
function that returns dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    """
    return obj.__dict__
