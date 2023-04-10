#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing the rectangle
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets width's attributes"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width's attributes"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Gets height's attributes"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height's attributes"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self) -> str:
        """Prints the diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ''
        rectangle = ''
        for c in range(self.__height):
            for r in range(self.__width):
                rectangle += '#'
            if c < self.__height - 1:
                rectangle += '\n'
            return rectangle
