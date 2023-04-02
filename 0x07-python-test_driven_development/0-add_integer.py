#!/usr/bin/python3
""" Module that adds two integers."""
def add_integer(a, b=98):
    """ Returns the sum of the two integers
        Floats are typecasted to integers before addition is done

        Args:
            a: first argument
            b: second argument

        Raises:
            TypeError: if either arguments is not an integer or a float
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))