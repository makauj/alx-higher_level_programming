#!/usr/bin/python3
"""pascal's triangle"""


def pascal_triangle(n):
    """return a list of integers representing Pascal's Triangle of n"""
    if n <= 0:
        return []
    """first row of the triangle"""
    triangle = [[1]]

    while len(triangle) != n:
        """get the last row"""
        tri = triangle[-1]
        """Each new row starts with a 1"""
        tmp = [1]

        for i in range(len(tri) - 1):
            """sum the two elements above"""
            tmp.append(tri[i] + tri[i + 1])

        """end each row with a 1"""
        tmp.append(1)
        """add the new row to the triangle"""
        triangle.append(tmp)
    return triangle
