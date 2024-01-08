#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclasses Rectangle and Square
"""


class BaseGeometry:
    """
    A base class for geometry-related operations.

    This class provides public instance methods 'area' and 'integer_validator'.
    """

    def area(self):
        """
        Placeholder method for calculating the area.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is an integer greater than 0.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A subclass of BaseGeometry representing a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes an instance of Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns an informal string representation of the rectangle.

        Returns:
            A string representing the rectangle in the format [Rectangle] width/height.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


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

    def __str__(self):
        """
        Returns an informal string representation of the square.

        Returns:
            A string representing the square in the format [Square] size/size.
        """
        return f"[Square] {self.__size}/{self.__size}"
