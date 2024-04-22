#!/usr/bin/python3
"""square module"""

from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """construct a square
            Args:
            size: size of square
            x: x position of square
            y: y position of square
            id: id of square
        """

        super().__init__(id, x, y, size, size)
        self.size = size
        self.x = x
        self.y = y
        self.id = id

    def __str__(self):
        """Returns a strin are"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
