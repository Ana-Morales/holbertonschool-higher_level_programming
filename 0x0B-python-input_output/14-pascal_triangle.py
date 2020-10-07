#!/usr/bin/python3
"""Funciton that  returns a list of lists of integers representing the Pascals
triangle of n"""


def pascal_triangle(n):
    """Pascal triangle of n"""
    if n <= 0:
        ls = []
        return ls
    if n == 1:
        ls = [[1]]
        return ls
    if n == 2:
        ls = [[1], [1, 1]]
        return ls
    if n > 2:
        ls = [[1], [1, 1]]
        flag = 1
        for i in range(3, n+1):
            ls_r = []
            for e in range(i):
                if e == 0 or e == i - 1:
                    ls_r.append(1)
                else:
                    ls_r.append(ls[flag][e-1] + ls[flag][e])
            flag += 1
            ls.append(ls_r)
        return ls
