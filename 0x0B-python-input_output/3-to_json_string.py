#!/usr/bin/python3
import json
"""defining function"""


def to_json_string(my_obj):
    """function that returns the JSON representation
    of an object (string)
    """
    return json.dump(my_obj)

