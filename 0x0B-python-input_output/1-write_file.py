#!/usr/bin/python3
"""Module that writes string to a file"""

def write_file(filename='', text=''):
    """Writes string to a text file
    Args:
        filename: name of the file
        text: text to be written

    Return: number of bytes written"""

    with open(filename, mode='w', encoding='UTF-8') as f:
        return (f.write(text))
