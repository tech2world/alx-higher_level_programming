#!/usr/bin/python3
"""Module that appends to a file"""


def append_write(filename='', text=''):
    """Appends string at the end of a file
    Args:
        filename: name of the file
        text: Text to be added to the end of the line
    Return: number of bytes written
    """

    with open(filename, mode='a', encoding='UTF-8') as f:
        return f.write(text)
