#!/usr/bin/python3
# a function that prints a dictionary by ordered keys.

def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = dict(sorted(a_dictionary.items()))
    for key, value in sorted_dictionary.items():
        print("{}: {}".format(key, value))
