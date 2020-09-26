#!/usr/bin/python3
"""Module 5-text_indentation
This module defines a function that prints a text with 2 new lines after
each of these characters: ., ? and :

"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these chars: ., ? and :
    """

    if type(text) != str:
        raise TypeError("text must be a string")
    s = text.replace(".", ".\n\n")
    s = s.replace(":", ":\n\n")
    s = s.replace("?", "?\n\n")
    ls = s.splitlines(True)
    ls_strip = []
    for line in ls:
        if line == "\n":
            ls_strip.append("\n")
        else:
            ls_strip.append(line.lstrip())
    print("".join(ls_strip), end="")
