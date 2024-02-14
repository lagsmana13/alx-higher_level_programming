#!/usr/bin/python3
"""
This is the "text_indentation" module.
The text_indentation module supplies one function, text_indentation.

Modified on 2024-01-03.

The text_indentation function takes a text (a string) and splits it into lines based on the characters "?", ":", and ".".
Each line is followed by two new lines.
"""

def text_indentation(text):
    """Splits a text into lines along "?", ":", and "." followed by two new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
