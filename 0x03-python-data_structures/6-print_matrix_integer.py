#!/usr/bin/python3

def print_matrix_integer(matrix=None):
    if matrix is None:
        return  # Added a check for None and return early

    for row in matrix:
        print(" ".join(str(element) for element in row))  # Used str() instead of "{:d}".format()
