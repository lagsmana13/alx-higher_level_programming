#!/usr/bin/python3
"""
This is the "matrix_divide" module.
The matrix_divide module defines a function to divide a matrix by a scalar integer.

Modified on 2024-01-03.

The matrix_divided function takes a matrix (a list of lists) and a divisor (an integer or float).
It divides each element of the matrix by the divisor and rounds the result to two decimal places.
The function returns the resulting matrix.
"""

def matrix_divided(matrix, div):
    """Divides matrix by scalar integer, rounded to two decimal places"""
    import decimal
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_msg)
    len_rows = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)
        len_rows.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error_msg)
        row_count += 1
    if len(set(len_rows)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_matrix
