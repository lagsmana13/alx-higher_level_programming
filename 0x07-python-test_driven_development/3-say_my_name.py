#!/usr/bin/python3
"""
This is the "say_my_name" module.
The say_my_name module supplies one function, say_my_name.

Modified on 2024-01-03.

The say_my_name function takes a first name (a string) and an optional last name (a string).
It prints "My name is" followed by the first name and last name.
If no last name is provided, only the first nameHere's the modified code:

```python
#!/usr/bin/python3
"""
This is the "3-say_my_name" module.
The 3-say_my_name module supplies one function, say_my_name.
Modified on 2024-01-03.

The say_my_name function takes a first name (a string) and an optional last name (a string).
It prints "My name is" followed by the first name and last name.
If no last name is provided, only the first name is printed.
"""

def say_my_name(first_name, last_name=""):
    """Prints "My name is" followed by the first name and optional last name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
