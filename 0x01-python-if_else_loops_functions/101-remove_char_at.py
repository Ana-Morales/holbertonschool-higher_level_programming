#!/usr/bin/env python3
def remove_char_at(str, n):
    if n >= 0 and n < len(str):
        str_copy = str.replace(str[n], "")
        return str_copy
    else:
        return str
