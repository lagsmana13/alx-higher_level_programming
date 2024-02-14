#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""
Defines a matrix multiplication function using NumPy.

The 101-lazy_matrix_mul module supplies one function, lazy_matrix_mul.

Modified on 2024-01-03.

The lazy_matrix_mul function takes two matrices (m_a and m_b) represented as lists of lists of integers or floats.
It performs matrix multiplication using NumPy's matmul function and returns the result.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices using NumPy's matmul function.
    
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    
    Returns:
        numpy.ndarray: The result of matrix multiplication.
    """
    return np.matmul(m_a, m_b)
