#!/usr/bin/python3
"""This module defines a a class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class, inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes the data"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Method to be used when use print on Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
