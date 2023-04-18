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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns list of JSON string representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        if type(list_dictionaries) != list or not all(type(i) == dict for i in list_dictionaries):
            raise TypeError('list_dictionaries must be a list dictionaries')
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write JSON representation to file"""
        file_name = '{}.json'.format(cls.__name__)
        with open(file_name, mode='w') as file_obj:
            if list_objs is None:
                file_obj.write('[]')
            else:
                list_dict = [o.to_dictionary() for o in list_objs]
                file_obj.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """return list of JSON representation"""
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        file_name = '{}.json'.format(cls.__name__)
        list_of_instances = []

        if os.path.exists(file_name):
            with open(file_name, mode='r', encoding='utf-8') as my_file:
                my_str = my_file.read()
                list_of_dictionaries = cls.from_json_string(my_str)
                for dictionary in list_of_dictionaries:
                    list_of_instances.append(cls.create(**dictionary))
        return list_of_instances
    