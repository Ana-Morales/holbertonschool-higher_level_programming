#!/usr/bin/python3
"""This module defines a function that appends a string to a text file
and returns the number of characters added"""


def append_write(filename="", text=""):
    """Appends a string to a text file and returns the number
    of characters added"""
    with open(filename, mode="a", encoding="utf-8") as f:
        num_chars = f.write(text)
    return num_chars
