#!/usr/bin/python3
"""
Contains the function "class_to_json" that returns a dictionary description of an object
with a simple data structure suitable for JSON serialization.
"""


def class_to_json(obj):
    """Returns a dictionary description with a simple data structure
    (list, dictionary, string, integer, and boolean)
    for JSON serialization of the provided object."""
    return obj.__dict__
