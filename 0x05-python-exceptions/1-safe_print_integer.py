def safe_print_integer(value):
    """Prints an integer if it is valid, otherwise returns False.

    Args:
        value: The value to print.

    Returns:
        bool: True if the value was printed, False otherwise.
    """

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
