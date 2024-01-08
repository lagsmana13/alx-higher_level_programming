#!/usr/bin/python3
"""
This module contains the MyList class, a subclass of list with additional functionality.
"""


class MyList(list):
    """A subclass of list that provides additional methods and behavior."""

    def __init__(self):
        """Initialize an instance of MyList."""
        super().__init__()

    def print_sorted(self):
        """Print the elements of the list in sorted order."""
        print(sorted(self))
