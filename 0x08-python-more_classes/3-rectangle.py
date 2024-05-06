#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Rectangle class
    Args:
    width: width of the rectangle
    height: height of the rectangle
    Returns: None
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """area method"""
        return self.width * self.height

    def perimeter(self):
        """perimeter method"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2
        

    def __str__(self):
        # return f"Area: {self.area()} - Perimeter: {self.perimeter()}"
        return self.print()

    def print(self):
        """Print in stdout the square with the character #.
        if size is 0: print empty line
        """
        for row in range(self.__height):
            for cloumn in range(self.__width):
                print('#', end="")
            print()
  
