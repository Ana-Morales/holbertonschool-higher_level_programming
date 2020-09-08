#!/usr/bin/python3
def no_c(my_string):
    t = list(my_string)
    i = 0
    while i < len(t):
        if t[i] == 'c' or t[i] == 'C':
            t.pop(i)
        i += 1
    return ''.join(t)
