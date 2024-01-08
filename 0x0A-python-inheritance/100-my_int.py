#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """
    A rebel version of an integer, perfect for opposite day!
    """

    def __new__(cls, *args, **kwargs):
        """
        Creates a new instance of the class.

        Returns:
            The new instance of MyInt.
        """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """
        Overrides the equality operator.

        Args:
            other: The object to compare with.

        Returns:
            True if self is not equal to other, False otherwise.
        """
        return int(self) != other

    def __ne__(self, other):
        """
        Overrides the inequality operator.

        Args:
            other: The object to compare with.

        Returns:
            True if self is equal to other, False otherwise.
        """
        return int(self) == other
