#!/usr/bin/python3

"""square module"""


class Square():
    """Define square class"""

    def __init__(self, size=0):
        """Construct
        Args: size
        Raise:
            TypeError:size must be an integer
            ValueError:size must be >= 0
        """

        def size(self):
            """this getter method for square size."""
            return self.__size

        def size(self, value):
            """this setter method for square size."""
            self.__size = value

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Return: current square area"""
        return self.__size ** 2
