#!/usr/bin/python3
"""This module writes a class Square that defines a square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data"""

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getting position value"""

        return self.__position

    @position.setter
    def position(self, value):
        """Setting position value"""
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of a square"""

        return self.__size * self.__size

    def my_print(self):
        """Prints the square with # character"""

        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for j in range(self.__size):
                print(" " * self.__position[0], "#" * self.__size, sep="")
