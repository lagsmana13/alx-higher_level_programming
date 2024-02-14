#!/usr/bin/python3
"""
This is the "print_square" module.
The print_square module supplies one function, print_square.

Modified on 2024-01-03.

The print_square function takes a size (an integer) and prints a square made of "#" characters.
The square has a length and width equal to the size.
"""

def print_square(size):
    """Prints a square made of "#" characters with a length of size"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
