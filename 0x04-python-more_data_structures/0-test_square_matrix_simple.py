#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return (matrix)
    square_list_lambda = lambda y: x**2 for x in y
    square_list = list(map(square_list_lambda, for y in matrix))
    return (square_list)

