#!/usr/bin/python3
"""
This module contains the is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specific class
    or an instance of a class inherited from it.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the specified class
        or an instance of a class inherited from it, False otherwise.
    """
    return isinstance(obj, a_class)
