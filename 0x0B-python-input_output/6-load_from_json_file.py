#!/usr/bin/python3
"""Module that creates object from json"""


import json


def load_from_json_file(filename):
    """loads object from JSON file"""

    with open(filename, mode='r') as js_file:
        js_obj = json.load(js_file)
        return js_obj
