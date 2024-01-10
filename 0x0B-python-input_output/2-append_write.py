#!/usr/bin/python3
"""
Contains the function "append_write" that appends a string to a file.
"""


def append_write(filename="", text=""):
    """Appends the provided "text" to the file specified by "filename" and returns the number of characters added."""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
