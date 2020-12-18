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
    if ls[m + 1] >= ls[m]:
        return find_peak(ls[m:])
    else:
        return find_peak(ls[:m])
