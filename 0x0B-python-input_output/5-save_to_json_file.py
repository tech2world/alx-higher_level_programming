#!/usr/bin/python3
"""Module that writes obj to text file using JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """Writes obj to text using json representation
    Args:
        my_obj: Object to be serialized
        filename: name of the file where string is stored
    """

    with open(filename, mode='w') as js_file:
        json.dump(my_obj, js_file)
