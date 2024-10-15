#!/usr/bin/python3
"""student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """initialize a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieve a dictionary representations of a Student"""
        return self.__dict__
