#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = str
    if n >= 0 and n < len(str):
        str_copy = str.replace(str[n],"")
    return str_copy
