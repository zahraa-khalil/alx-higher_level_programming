#!/usr/bin/python3
"""Module add integer"""


def add_integer(a, b=98):
    """Adds two integers
    Args: 
        a: f integer
        b: s integer, default: 98

    Raises:
        TypeError: if a || b not integers or floats,
    
    Returns: 
        a + b
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/0-add_integer.txt")