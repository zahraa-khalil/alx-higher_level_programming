#!/usr/bin/python3
"""Square module"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Construct
        args:
            size: integer size of a side of a square.
            Raise:
                TypeError:size must be an integer
                ValueError:size must be >= 0

            Returns: current square area

        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Return the size of the square"""
        return self.__size**2
