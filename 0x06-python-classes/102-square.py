#!/usr/bin/python3
"""This module writes a class Square that defines a square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes the data
        Args:
            size: size of the square
        """

        self.size = size

    @property
    def size(self):
        """Getting size value"""

        return self.__size

    @size.setter
    def size(self, value):
        """Setting size value"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square"""

        return self.__size * self.__size
    def __eq__(self, other):
        """Return True if self and other are equal"""

        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if self is different from other"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Return True if self is grater than other"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if self is grater or equal than other"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Return True if self is less than other"""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if self is less or equal than other"""
        return self.area() <= other.area()
