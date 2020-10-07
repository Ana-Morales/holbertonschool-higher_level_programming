#!/usr/bin/python3
"""This module defines a function that reads n lines of a text file
and prints it to stdout"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file"""
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            i = 0
            while i < nb_lines:
                line = f.readline()
                if not line:
                    break
                print(line, end="")
                i += 1
