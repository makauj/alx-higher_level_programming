#!/usr/bin/python3
"""Function that ddefines a matrix division function"""


def matrix_divided(matrix, div):
    """Check if matrix is a list of lists of integers or floats
    Args:
        matrix: composed of lists, elements in list are numbers
        div: the divisor
    Raise exceptions:
        TypeError: if elements in lists are not numbers
        TypeError: if rows are not the same size
        TypeError: if div is not a number
        ZeroDivisionError: If div == 0
    Returns:
        A new matrix with divided values
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(el, (int, float))
                for el in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        "integers/floats")

    """Check if all rows in the matrix are of the same size"""
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    """Check if div is a number"""
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    """Check if div is zero"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """Create and return the new matrix with divided values"""
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
