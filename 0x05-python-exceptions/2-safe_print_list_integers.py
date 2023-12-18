def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list of integers, or the entire list if x is not specified.

    Args:
        my_list (list): The list to print.
        x (int, optional): The number of elements to print. Defaults to 0, which prints the entire list.

    Returns:
        int: The number of elements printed.
    """

    n = 0
    for i, item in enumerate(my_list):
        if i < x:
            try:
                print("{:d}".format(item), end="")
                n += 1
            except (ValueError, TypeError):
                continue
        else:
            break

    print()
    return n
