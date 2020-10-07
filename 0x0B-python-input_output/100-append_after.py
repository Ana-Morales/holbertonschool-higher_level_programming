#!/usr/bin/python3
"""This module defines a function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file"""
    with open(filename, encoding="utf-8") as f:
        ls_lines = []
        while True:
            line = f.readline()
            if not line:
                break
            ls_lines.append(line)
            if line.find(search_string) != -1:
                ls_lines.append(new_string)
    with open(filename, mode="w", encoding="utf-8") as f:
        f.writelines(ls_lines)
