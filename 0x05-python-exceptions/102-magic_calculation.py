def magic_calculation(a, b):
    """Performs a calculation based on the values of a and b.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The result of the calculation.
    """

    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')

            result += a ** b / i
        except:
            result = b + a
            break

    return result
