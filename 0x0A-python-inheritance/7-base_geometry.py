#!/usr/bin/python3
"""This module defines a a class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
