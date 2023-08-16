#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return (matrix)
    square_list_lambda = lambda x: x**2
    square_list = []# list(map(square_list_lambda, matrix))
    for x in matrix:
        square_list.append(list(map(square_list_lambda, x)))
    return (square_list)

#    if len(matrix) == 0:
#        return (matrix)
#    square_matrix =[] #[x**2 for y in matrix for x in y]
#    for y in matrix:
#        mat = []
#        for x in y:
#            mat.append(x**2)
#        square_matrix.append(mat)
#
#    return (square_matrix)
