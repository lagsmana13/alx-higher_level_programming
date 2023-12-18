def safe_function(fct, *args):
    """Executes a function and prints an error message to stderr if an exception occurs.

    Args:
        fct: The function to execute.
        *args: The arguments to pass to the function.

    Returns:
        The return value of the function, or None if an exception occurred.
    """

    try:
        r = fct(*args)
        return r
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
