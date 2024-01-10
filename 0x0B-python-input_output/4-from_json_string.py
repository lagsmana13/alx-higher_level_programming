#!/usr/bin/python3
"""
Contains the function "from_json_string" that converts a JSON string to an object.
"""

import json


def from_json_string(my_str):
    """Returns an object represented by the provided JSON string."""
    return json.loads(my_str)
