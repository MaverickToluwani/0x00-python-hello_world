#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        for j in range(col):
            if j == col-1:
                print("{}".format(matrix[i][j]), end="")
            else:
                print("{}".format(matrix[i][j]), end=" ")
        print("")
