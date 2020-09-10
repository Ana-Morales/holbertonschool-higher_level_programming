#!/usr/bin/python3
def best_score(a_dictionary):
    lst = list()
    if a_dictionary is None or len(list(a_dictionary.items())) == 0:
        return None
    for k, v in list(a_dictionary.items()):
        lst.append((v, k))
    lst.sort(reverse=True)
    return lst[0][1]
