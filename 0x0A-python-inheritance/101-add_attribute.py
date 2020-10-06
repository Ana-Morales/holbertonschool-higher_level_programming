#!/usr/bin/python3
"""This module defines  a function that adds a new attribute to an object
 if its possible"""


def add_attribute(clss, atrb, val):
    """adds a new attribute to an object if its possible"""

    if "__dict__" in dir(clss):
        setattr(clss, atrb, val)
    else:
        raise TypeError("can't add new attribute")
