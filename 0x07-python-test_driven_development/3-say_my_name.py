#!/usr/bin/python3
""" A  module with a function that prints name."""


def say_my_name(first_name, last_name=""):
    """ Prints a <firstname> <lastname>

    Args:
        first_name (str): the first name to be printed
        last_name (str): the last name to be printed

    raises:
        TypeError: if either first_name or last_name are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
