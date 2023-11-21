#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[0 for size in range(len(row))]for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new[i][j] = matrix[i][j] ** 2
    return new