#!/usr/bin/python3
"""Square Module"""


class Square():
    """Define a class called Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Construct
        Args:
            size: size of sede of square.
            position (int, int): position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter to retriefe size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to set size of square
        raise Typeerror if size is not int
        raise ValueError if size is less than or equal 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Getter to return position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter to set position of square"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Return area of square"""
        return self.__size ** 2

    def my_print(self):
        """Print square to stdout with the character #
        print an empty line if size == 0
        """

        if self.__size == 0:
            print()
            return

        if self.__position[1] > 0:
            print("\n" * (self.__position[1] - 1))

        for row in range(0, self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
