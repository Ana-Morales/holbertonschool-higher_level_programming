#!/usr/bin/python3
"""
Module 0-add_integer.py
This module defines a function that adds two numbers

"""


def add_integer(a, b=98):
    """Returns the sum of a + b
    a and b must be integers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
