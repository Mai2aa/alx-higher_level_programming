#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[]]
    for i in matrix:
        for j in i:
            new.append(j ** 2)
    return new
