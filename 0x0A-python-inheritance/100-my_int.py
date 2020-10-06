#!/usr/bin/python3
"""This module defines a class MyInt that inherits from int"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __eq__(self, other):
        """Return True if self and other are NOT equal"""
        return int(self) != other

    def __ne__(self, other):
        """Return True if self and other are equal"""
        return int(self) == other
