#!/usr/bin/python3
"""Find a peak"""


def find_peak(ls):
    """Finds a peak in a list of unsorted integers"""

    length = len(ls)
    if length == 0:
        return None
    if length == 1:
        return ls[0]
    m = length // 2
    if m == length - 1:
        if ls[m] > ls[m - 1]:
            return ls[m]
        return ls[m - 1]
    if ls[m] > ls[m + 1] and ls[m] > ls[m - 1]:
        return ls[m]
    else:
        l_m = find_peak(ls[:m])
        l_r = find_peak(ls[m + 1:])
        if l_m > l_r:
            return l_m
        return l_r
