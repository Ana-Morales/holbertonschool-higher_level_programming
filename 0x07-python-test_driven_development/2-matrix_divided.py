#!/usr/bin/python3
"""
Module 2-matrix_divided.py
This module defines a function that divides all elementes of a matrix

"""


def matrix_divided(matrix, div):
    """Returns the division of all elementes in matrix by a given number
    matrix must be a list of lists of ints or floats
    Each row of the matrix must be of the same size
    div must be a number (integer or float)
    div cant be equal to 0
    Returns a new matrix
    """
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    for i in range(len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for i in range(len(matrix)):
        if i < (len(matrix) - 1):
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError("Each row of the matrix must \
have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    mtx = list(map(lambda r: list(map(lambda x: round(x/div, 2), r)), matrix))
    return mtx
