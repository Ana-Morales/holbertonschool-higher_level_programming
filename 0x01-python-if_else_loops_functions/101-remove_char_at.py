#!/usr/bin/env python3
def remove_char_at(str, n):
    str_copy = str
    if n >= 0 and n < len(str):
        str_copy = str_copy.replace(str_copy[n], "")
    return str_copy
