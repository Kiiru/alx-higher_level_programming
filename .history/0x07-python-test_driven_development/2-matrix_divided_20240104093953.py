#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Matrix divide function

    Args:
        matrix: multidimentional array
        div: number (int or float)

    Returns:
        a new matrix
    """
    if div == 0:
        raise ZeroDivisionError('division by zero')
    
    if not matrix:
        return matrix
    
    if not check_matrix_rows(matrix):
        raise TypeError('Each row of the matrix must have the same size')
    nMatrix = []
    for item in matrix:
        row = []
        for nItem in item:
            if not isinstance(nItem, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            val = nItem / div
            row.append(val)
        nMatrix.append()
        
    
def check_matrix_rows(matrix):
    """ Check Matrix rows function

    Args:
        matrix: multidimentional array

    Returns:
        True if all Rows are equal, False if they are not
    """
    if not matrix:
        return False
    first_row_length = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != first_row_length:
            return False
    
    return True