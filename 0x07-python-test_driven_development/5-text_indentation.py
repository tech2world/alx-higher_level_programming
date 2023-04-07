#!/usr/bin/python3
""" A module with a function that indents text."""


def text_indentation(text):
    """ Prints text with two new lines after each of these characters '.', '?', ':'

    Args:
        text (str): The string to be printed

    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while count < len(text) and text[count] == " ":
        count += 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count += 1
            while count < len(text) and text[count] == " ":
                count += 1
            continue
        count = count + 1