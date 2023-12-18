def safe_print_integer_err(value):
    """Prints an integer if it is valid, otherwise prints an error message to stderr and returns False.

    Args:
        value: The value to print.

    Returns:
        bool: True if the value was printed, False otherwise.
    """

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return False
