#!/usr/bin/python3
"""Base Module"""

import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert list of dictionaries"""
        """Construct
        Args:
            list_dictionaries: list of dictionaries
            return: json string or []
        """
        if (list_dictionaries) is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string to a file"""
        """Construct
        Args:
            list_objs: list of objects
            return: None
        """
        # filename = cls.__name__ + ".json"
        # with open(filename, 'w',  encoding='utf-8') as f:
        #     f.write(cls.to_json_string(list_objs))

        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string.

        Args:
        json_string (str): _description_

        Returns:
        list: JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)

        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Loads a dictionary from
        Args: cls
        Returns: list of instances"""
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins
