#!/usr/bin/python3
"""Module that reads file """

def read_file(filename=''):
    """Reads a text file and print to stdout"""

    with open(filename, mode='r', encoding='UTF-8') as f:
        for line in f:
            print(line, end='')
