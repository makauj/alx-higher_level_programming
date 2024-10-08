#!/usr/bin/python3
"""A function to find the max integer"""


def max_integer(list=[]):
    length = len(list)

    if length == 0:
        return None
    result = list[0]
    i = 1
    while i < length:
        if list[i] > result:
            result = list[i]
        i += 1
    return result
