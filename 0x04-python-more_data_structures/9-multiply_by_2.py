#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = dict()
    for k in a_dictionary:
        new_d[k] = a_dictionary.get(k) * 2
    return new_d
