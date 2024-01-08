#!/usr/bin/python3
"""
This module contains the lookup function.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of attribute and method names as strings.
    """
    return dir(obj)
