#!/usr/bin/python3
"""square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """construct a square
            Args:
            size: size of square
            x: x position of square
            y: y position of square
            id: id of square
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method for size of square"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
