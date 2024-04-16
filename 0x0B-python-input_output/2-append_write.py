#!/usr/bin/python3
"""defining write_file function"""


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text file
    and returns the number of characters added:
    """
    with open(filename, 'a',  encoding='utf-8') as f:
        return f.write(text)
