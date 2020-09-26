#!/usr/bin/python3
"""Module 3-say_my_name
This module defines a function that prints
My name is <first name> <last name>

"""


def say_my_name(first_name, last_name=""):
    """
    Prints: My name is <first name> <last name>
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    return print("My name is {} {}".format(first_name, last_name))
