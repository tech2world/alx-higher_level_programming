#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Representation of a rectangle"""

    def __int__(self, width=0, height=0):
        """Initializing the rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Defines the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width's attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Defines the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height's attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        # noinspection PyAttributeOutsideInit
        self.__height = value
