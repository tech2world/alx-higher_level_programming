#!/usr/bin/python3
""" Square Module"""


class Square:
    """ Defines a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represents size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Retrieves size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns: area os square"""

        return (self.__size ** 2)

    def my_print(self):
        """Prints the square using #"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print('#' * self.__size)
