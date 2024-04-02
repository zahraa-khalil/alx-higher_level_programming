#!/usr/bin/python3
"""Square Module"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Constructor:
        args:
             size: Integer. length of a side of the square
         Raises:
             TypeError:size must be an integer
             ValueError:size must be >= 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
