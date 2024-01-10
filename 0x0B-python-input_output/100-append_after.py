#!/usr/bin/python3
"""
Contains the function "append_after" to append a string after a line containing a search string in a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends the "new_string" after a line containing the "search_string" in the specified "filename".

    Args:
        filename (str): The name of the file to modify. Default is an empty string.
        search_string (str): The string to search for in the file's lines. Default is an empty string.
        new_string (str): The string to append after the line containing the search string. Default is an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        line_list = []
        while True:
            line = f.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(line_list)
