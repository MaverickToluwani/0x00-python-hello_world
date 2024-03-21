#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqrmatrix = []
    for row in matrix:
        new_row = list(map(lambda x: x**2, row))
        sqrmatrix.append(new_row)
    return sqrmatrix
