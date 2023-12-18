def safe_print_division(a, b):
    """Prints the division of two numbers, or None if there is a ZeroDivisionError.

    Args:
        a (int, float): The dividend.
        b (int, float): The divisor.

    Returns:
        float: The result of the division, or None if there was a ZeroDivisionError.
    """

    try:
        div = a / b
    except ZeroDivisionError:
        div = None
    finally:
        print("Inside result: {}".format(div))

    return div
