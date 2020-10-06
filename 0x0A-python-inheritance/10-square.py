#!/usr/bin/python3
"""This module defines a a class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Initializes data"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of a square"""
        return self.__size * self.__size
