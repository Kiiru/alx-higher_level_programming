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
    
def check_matrix_rows(matrix):
    """ Check Matrix rows function

    Args:
        matrix: multidimentional array

    Returns:
        True if all Rows are equal, False if they are not
    """
    if not matrix:
        return False
    first_row_length = len()