#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A subclass of Rectangle representing a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size):
        """
        Initializes an instance of Square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square (size ** 2).
        """
        return self.__size ** 2
