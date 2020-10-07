#!/usr/bin/python3
"""This module defines a function that writes a string to a text file
and returns the number of characters written"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns the number
    of characters written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        num_chars = f.write(text)
    return num_chars
