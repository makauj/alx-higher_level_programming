#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Return list of integers containing all peaks found in a list
    """
    peaks = []
    n = len(list_of_integers)

    if n == 0:
        return None

    if n == 1 or list_of_integers(0) >= list_of_integers:
        peaks.append(list_of_integers[0])

    for i in range(1, n - 1):
        if (list_of_integers[i] >= list_of_integers[i - 1]
                and list_of_integers[i] >= list_of_integers[i + 1]):
            peaks.append(list_of_integers[i])

    if n > 1 and list_of_integers[n - 1] >= list_of_integers[n - 2]:
        peaks.append(list_of_integers[n - 1])

    return peaks
