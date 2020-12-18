#!/usr/bin/python3
"""Find a peak"""


def find_peak(ls):
    """Finds a peak in a list of unsorted integers"""

    if len(ls) == 0:
        peak = None
    else:
        peak = ls[0]
        for i in range(1, len(ls)):
            if i == len(ls) - 1:
                break
            if ls[i] > ls[i - 1] and ls[i] > ls[i + 1]:
                peak = ls[i]
                break
            if ls[i] == ls[i + 1] and peak > ls[i]:
                break
    return peak
