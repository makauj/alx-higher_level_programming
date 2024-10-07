#!/usr/bin/python3

def matrix_divided(matrix, div):
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(el, (int, float)))
                for el in [num for row in matrix for num in row])):
          raise TypeError("matrix must be a matrix (list of lists) of"
                          "integers/floats")
    