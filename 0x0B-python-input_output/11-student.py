#!/usr/bin/python3
"""Simple implementation of a serialization and deselialization mechanism
(concept of representation of an object to another format, without
losing any information and allow us to rebuild an object based on this
representation)
"""


class Student:
    """syudent class"""

    def __init__(self, first_name, last_name, age):
        """initialize new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve dictionary representation of a student instance"""
        if type(attrs) is list and all(type(ele) is str for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        replace all attributes of a student instance
        dictionary key - public attribute name
        dictionary value - public attribute value
        """
        for key, value in json.items():
            setattr(self, key, value)
