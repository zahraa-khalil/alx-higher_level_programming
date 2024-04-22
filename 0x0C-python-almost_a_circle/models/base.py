#!/usr/bin/python3
"""Base Module"""

import json


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

    def to_json_string(list_dictionaries):
        """Convert list of dictionaries"""
        """Construct 
        Args:
            list_dictionaries: list of dictionaries
            
            return: json string or [] """
        if (list_dictionaries) == None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)
