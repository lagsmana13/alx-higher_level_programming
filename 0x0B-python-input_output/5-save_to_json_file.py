#!/usr/bin/python3
"""
Contains the function "save_to_json_file" that writes an object to a text file using JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """Writes the provided object to a text file specified by "filename" using JSON representation."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
