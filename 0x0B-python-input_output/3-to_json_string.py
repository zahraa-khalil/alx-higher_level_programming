#!/usr/bin/python3
"""defining function"""


import json


def to_json_string(my_obj):
    """function returns JSON representation
    of an object
    """
    return json.dumps(my_obj)
