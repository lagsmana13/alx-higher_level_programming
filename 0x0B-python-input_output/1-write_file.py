#!/usr/bin/python3
"""
Contains the function "write_file"
"""


def write_file(filename="", text=""):
    """Returns the number of characters written to the file specified by "filename" from "text"."""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
