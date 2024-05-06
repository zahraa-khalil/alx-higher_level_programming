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
        self._width = width
        self._height = height

    @property
    def width(self):
        """width getter"""
        return self._width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    @property
    def height(self):
        """height getter"""
        return self._height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value
