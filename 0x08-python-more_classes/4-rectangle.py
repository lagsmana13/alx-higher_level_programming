#!/usr/bin/python3
"""
Defines a class Rectangle.
"""


class Rectangle:
    """Representation of a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the private instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private instance attribute width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the private instance attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private instance attribute height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns a printable string representation of the rectangle."""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """Returns a string representation of the rectangle for reproduction."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
