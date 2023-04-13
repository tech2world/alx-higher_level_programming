#!/usr/bin/python3
"""MOdule taht writes obj to text file using JSON representattion"""


import json


def save_to_json_file(my_obj, filename):
    """Writes obj to text using json representation"""

    with open(filename, mode='w') as js_file:
        json.dump(my_obj, js_file)
