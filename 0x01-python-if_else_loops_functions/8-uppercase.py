def convert_to_uppercase(string):
    """Convert a string to uppercase."""
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
