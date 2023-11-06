#!/usr/bin/python
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            print(('{:d}'.format(j)), end=' ')
        print(''.format())
