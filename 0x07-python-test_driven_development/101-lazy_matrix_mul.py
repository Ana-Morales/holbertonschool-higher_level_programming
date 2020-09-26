#!/usr/bin/python3
"""Module that multiplies 2 matrices using numpy:
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices
    """
    return np.matmul(m_a, m_b)
