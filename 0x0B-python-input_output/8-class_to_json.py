#!/usr/bin/python3
"""defining function"""


def class_to_json(obj):
    """ function that returns the dictionary description
    with simple data structure for JSON serialization of an object:
    """
    return {attr: getattr(obj, attr) for attr in obj.__dict__ if isinstance(getattr(obj, attr), (list, dict, str, int, bool))}
