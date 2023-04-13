#!/usr/bin/python3
"""Module that returns a JSON Object"""


import json


def to_json_string(my_obj):
    """Return json representation of an object"""

    return json.dumps(my_obj)
