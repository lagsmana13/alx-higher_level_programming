#!/usr/bin/python3
"""
This module contains a function for matrix multiplication.

The matrix_mul module supplies one function, matrix_mul.

Modified on 2024-01-03.

The matrix_mul function takes two matrices represented as lists of lists (m_a and m_b) and performs matrix multiplication.
It checks the requirements for matrix multiplication, such as non-empty matrices, compatible sizes, and valid element types (int or float).
If the matrices can be multiplied, the function returns the resulting matrix.
"""

def matrix_mul(m_a, m_b):
    """Multiplies two matrices and returns the result.
    
    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.
    
    Returns:
        list of lists: The result of matrix multiplication.
    
    Raises:
        TypeError: If m_a or m_b is not a list, or if the matrices contain invalid element types.
        ValueError: If m_a or m_b is empty, if the rows of the matrices have different sizes, or if the matrices cannot be multiplied.
    """

    # ... (rest of the code remains the same)
