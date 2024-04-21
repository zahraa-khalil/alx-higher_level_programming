#!/usr/bin/python3
"""Base Module"""


class Base:
    """Base class: base of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor
        Args:
            id: id of object
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            

    # def __repr__(self):
    #     return f"Base(id={self.id})"
