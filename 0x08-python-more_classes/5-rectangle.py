#!/usr/bin/python3
"""This module writes a class Rectangle that defines a rectangle
"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the data"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting width value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting height value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Method to be used when use print on Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("#"*self.__width + "\n") * (self.__height - 1)\
            + ("#"*self.__width)

    def __repr__(self):
        """repr method"""
        return "Rectangle(" + str(self.__width) + \
            ", " + str(self.__height) + ")"

    def __del__(self):
        """Destructor"""
        print("Bye rectangle...")
