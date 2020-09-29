#!/usr/bin/python3
"""Module thatwrites aclass LockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name."""


class LockedClass:
    """Class LockedClass"""
    __slots__ = ["first_name"]
