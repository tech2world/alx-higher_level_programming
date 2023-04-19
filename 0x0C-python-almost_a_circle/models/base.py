#!/usr/bin/python3
"""Module for a Base class of all other classes within its scope"""
import csv
import json
import os
import turtle


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

    @classmethod
    def save_to_file(cls, list_objs):
        """"Serializes list_objs and save to file"""
        file_name = '{}.csv'.format(cls.__name__)
        with open(file_name, mode='w', newline='') as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV file from a file"""
        file_name = '{}.csv'.format(cls.__name__)
        try:
            with open(file_name, mode='r', newline='') as csv_file:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                list_dicts = csv.DictReader(csv_file, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items()) for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using turtle module.
        Args:
            list_rectangles: a list of Rectangle objects to draw
            list_squares: a list od square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor('#b7312c')
        turt.pensize(3)
        turt.shape('turtle')

        turt.color('#ffffff')
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color('#b5e3d8')
        for sqr in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sqr.x, sqr.y)
            turt.down()
            for i in range(2):
                turt.forward(sqr.width)
                turt.left(90)
                turt.forward(sqr.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
