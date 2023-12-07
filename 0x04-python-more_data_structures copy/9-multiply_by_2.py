#!/usr/bin/python3

# function that returns a new dictionary with
# all values multiplied by 2
def multiply_by_2(a_dictionary):
    b_dictionary = {}
    for key, value in a_dictionary.items():
        b_dictionary[key] = value * 2
    return b_dictionary
