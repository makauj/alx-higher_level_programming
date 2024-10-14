#!/usr/bin/python3
"""MyInt module that inherits from int"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, value):
        """
        override the == operator so it behaves like != instead
        """
        return self.real != value
    
    def __ne__(self, value):
        """
        override != so it behaves like == instead
        """
        return self.real == value
