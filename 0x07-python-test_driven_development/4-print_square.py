#!/usr/bin/python3
""" A module with a function that prints a square."""
def print_square(size):
    """ prints a square with th e character #

    Args:
        size (int): represents the length of the square

    Raises:
        TypeError: if the size is not an integer
        TypeError: if the size is a float
        ValueError: if size is < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for n in range(size):
            print("#", end="")
        print("")
