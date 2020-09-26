#!/usr/bin/python3
"""Module 4-print_square
This module defines a function that prints a square with the character #

"""


def print_square(size):
    """
    Prints a square with the character #
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            print("#" * size)
