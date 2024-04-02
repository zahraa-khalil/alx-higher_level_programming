#!/usr/bin/python3

"""square module"""


class Square():
    """Define square class"""

    def __init__(self, size=0):
        """Construct
        Args: size
        """
        self.__size = size

    @property
    def size(self):
        """this getter method for square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """this setter method for square size.
        Raise:
            TypeError:size must be an integer
            ValueError:size must be >= 0
        """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return: current square area"""
        return self.__size ** 2
