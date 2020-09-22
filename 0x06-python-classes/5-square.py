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

    def my_print(self):
        """Prints the square with # character"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
