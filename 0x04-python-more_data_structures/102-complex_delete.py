#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in list(a_dictionary.values()):
        return a_dictionary
    ls = list(a_dictionary.keys())
    for key in ls:
        if a_dictionary.get(key) == value:
            del a_dictionary[key]
            ls = list(a_dictionary.keys())
    return a_dictionary
