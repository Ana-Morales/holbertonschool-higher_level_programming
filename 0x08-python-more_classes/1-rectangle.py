#!/usr/bin/python3
"""This Module writes a class Rectangle that defines a rectangle
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
