#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Rectangle class
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol: The print symbol
    Args:
    width: width of the rectangle
    height: height of the rectangle
    Returns: None
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
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
        return self.build_representation()

    def build_representation(self):
        """Print in stdout the Rectangle with the character #.
        if size is 0: print empty line
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(
            str(self.print_symbol) * self.width
            for _ in range(self.height)
        )

    def __repr__(self):
        return "Rectangle({0}, {1})".format(self.width, self.height)

    def __del__(self):
        """Prints message upon deletion of instance"""
        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
