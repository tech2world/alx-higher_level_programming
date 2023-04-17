#!/usr/bin/python3
"""A square module"""

from models.rectangle import Rectangle
class Square(Rectangle):
    """represents a square"""
    def __int__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__int__(size, size, x, y, id)

    def __str__(self):
        """returns string representation of the class"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'

    @property
    def size(self):
        """get value for size"""
        return 