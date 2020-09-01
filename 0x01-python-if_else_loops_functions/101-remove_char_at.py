#!/usr/bin/env python3
def remove_char_at(str, n):
    str_copy = str
    if n >= 0 and n < len(str):
        str_copy = str[:n] + str_copy[(n+1):]
    return str_copy
