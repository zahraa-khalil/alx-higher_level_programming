#!/usr/bin/python3
"""Function to find the peak of list of integers"""


def find_peak(list_of_integers):
    """Finds the peak of list of integers"""
    list_of_integers.sort()
    print(list_of_integers[-1])
    # return list_of_integers[-1]
