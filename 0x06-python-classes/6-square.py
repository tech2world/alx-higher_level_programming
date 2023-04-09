#!/usr/bin/python3
""" Square Module"""


class Square:
    """ Defines a square"""

    def __init__(self, size=0, position=0):
        """Initializing this square class
        Args:
            size: represents size of the square
            position: position of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """property of the co-ordinates of a square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Set position of the square
        Args:
            Value: tuple of two integers
        Raises:
            TypeError: if value is not a tuple of two positive ints
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not all(isinstance(num, int) for num in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not all(num >= 0 for num in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ Returns: area of square"""

        return (self.__size ** 2)

    def my_print(self):
        """Print square with # character"""

        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(' ', end='') for j in range(0, self.__position[0])]
            [print('#', end='') for k in range(0, self.__size)]
            print('')
