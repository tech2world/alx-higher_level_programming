#!/usr/bin/python3
"""A module that returns a simple data structure."""


def class_to_json(obj):
    """returns dictionary representation of simple data structure"""

    return obj.__dict__
