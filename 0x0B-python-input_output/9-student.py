#!/usr/bin/python3
"""Module for class Student"""


class Student:
    """
    A class that defines a student.
    Attributes:
        first_name: name of student.
        last_name: name of student.
        age: student's age.
    """

    def __int__(self, first_name, last_name, age):
        """initializes a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of a student"""
        return self.__dict__
