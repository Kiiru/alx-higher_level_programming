#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return (matrix)
    square_list = []
    for x in matrix:
        square_list.append(list(map(lambda x: x ** 2, x)))
    return (square_list)
