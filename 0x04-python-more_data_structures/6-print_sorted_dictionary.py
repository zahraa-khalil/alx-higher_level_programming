#!/usr/bin/python3
# a function that prints a dictionary by ordered keys.
# in only one set.
# set difference

def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = dict(sorted(a_dictionary.items()))
    for key, value in sorted_dictionary.items():
        print(key, ":", value)
