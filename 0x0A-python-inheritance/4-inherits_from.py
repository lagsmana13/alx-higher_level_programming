#!/usr/bin/python3
"""
This module contains the inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is a subclass of a specific class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is a subclass of the specified class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
