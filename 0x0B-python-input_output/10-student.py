#!/usr/bin/python3
"""A student class module"""


class Student:
    """A class that defines a student
    Attributes:
        first_name: student's first name
        last_name : student's last name
        age : student's age
    """
    def __int__(self, first_name, last_name, age):
        """Initializes the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """Gets a dictionary representation of Student
        Args:
            attr(list) : attribute list being received
        """
        if attr is not None:
            ret = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return ret
        else:
            return self.__dict__
