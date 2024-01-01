#!/usr/bin/python3
"""Matrix multiplication"""


def matrix_mul(m_a, m_b):
    # Check if m_a is a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    # Check if m_b is a list
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a is a list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    # Check if m_b is a list of lists
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a is empty
    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")

    # Check if m_b is empty
    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    # Check if m_a contains only integers or floats
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")

    # Check if m_b contains only integers or floats
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    # Check if m_a is a rectangle
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("Each row of m_a must be of the same size")

    # Check if m_b is a rectangle
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("Each row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            cell = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(cell)
        result.append(row)

    return result
