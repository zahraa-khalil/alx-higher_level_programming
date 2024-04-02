#!/usr/bin/python3

"""square module"""


class Square():
    """define square"""

    def __init__(self, size=0):
        """construct square
        Args: size
        """
        self.__size = size

    @property
    def size(self):
        """Size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size getter"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return Square Area"""
        return self.__size ** 2

    def my_print(self):
        """Print in stdout the square with the character #.
        if size is 0: print empty line
        """

        if self.__size == 0:
            print()
            return
        for row in range(self.__size):
            for cloumn in range(self.__size):
                print('#', end="")
            print()
