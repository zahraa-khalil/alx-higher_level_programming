#!/usr/bin/python3
"""defining function"""


import json


def class_to_json(obj):
    """ function that returns the dictionary description
    with simple data structure for JSON serialization of an object:
    """
    return json.dumps(obj.__dict__)
