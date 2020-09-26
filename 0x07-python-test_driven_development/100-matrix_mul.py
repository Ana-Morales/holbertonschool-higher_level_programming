#!/usr/bin/python3
"""Module that multiplies 2 matrices:
"""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    for i in range(len(m_a)):
        if type(m_a[i]) != list:
            raise TypeError("m_a must be a list of lists")
    for i in range(len(m_b)):
        if type(m_b[i]) != list:
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    len_a = 0
    for i in range(len(m_a)):
        len_a += len(m_a[i])
    if len_a == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    len_b = 0
    for i in range(len(m_b)):
        len_b += len(m_b[i])
    if len_b == 0:
        raise ValueError("m_b can't be empty")
    for element in m_a:
        for j in range(len(element)):
            if type(element[j]) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for element in m_b:
        for j in range(len(element)):
            if type(element[j]) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    for i in range(len(m_a)):
        if i != len(m_a) - 1:
            if len(m_a[i]) != len(m_a[i + 1]):
                raise TypeError("each row of m_a must be of the same size")
    for i in range(len(m_b)):
        if i != len(m_b) - 1:
            if len(m_b[i]) != len(m_b[i + 1]):
                raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    ls = []
    mul = []
    a = 0
    size = len(m_a)
    for i in range(size):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                a += m_a[i][k] * m_b[k][j]
            ls.append(a)
            a = 0
        mul.append(ls)
        ls = []
    return mul
