#!/usr/bin/python3
"""defining readfile function"""
def read_file(filename=""):
    """function that reads a text file (UTF8)"""

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
