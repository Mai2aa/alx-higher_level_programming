#!/usr/bin/python3
"""lazy matrix multiplication"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    try:
        result = np.matmul(m_a, m_b)
    except ValueError:
        raise InvalidMatrixMultiplicationError("m_a and m_b \
            can't be multiplied")
    return result


class InvalidMatrixMultiplicationError(Exception):
    def __init__(self, message):
        self.message = message
