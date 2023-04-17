#!/usr/bin/python3
"""Module for a Base class of all other classes within its scope"""


import json
import os


class Base:
    """Base of all classes created"""

    __nb_objects = 0

    def __int__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
