#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes of the rectangle object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Getter functions
    @property
    def width(self):
        """Gets value for width"""
        return self.__width

    @property
    def height(self):
        """Gets value for height """
        return self.__height

    @property
    def x(self):
        """Gets value for x"""
        return self.__x

    @property
    def y(self):
        """Gets value for y"""
        return self.__y

    # setter functions
    @width.setter
    def width(self, value):
        """sets width's value"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """gets height's value"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """gets value for x"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """gets value for y"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """represents the area of a rectangle"""
        return self.__height * self.__width

    def display(self):
        """Display rectangle using #"""
        for y in range(self.y):
            print('')
        for h in range(self.__height):
            for x in range(self.x):
                print(" ", end='')
            for w in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """prints a string representation of the rectangle object"""
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
            {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        """Updates the attributes of the Rectangle"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Returns a dictionary representation of the Rectangle"""
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
