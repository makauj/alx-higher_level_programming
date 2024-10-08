#!/usr/bin/python3
"""Python3 module"""


class LockedClass():
    """Prevent dynamic attribute creation"""
    __slots__ = ["first_name"]

    def __init__(self):
        """do nothing unless attribute first_name"""
        pass
