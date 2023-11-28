#!/usr/bin/python3
def is_lowercase(character):
    """Function checks for lowercase characters."""
    if ord(character) >= 97 and ord(character) <= 122:
        return True
    else:
        return False
