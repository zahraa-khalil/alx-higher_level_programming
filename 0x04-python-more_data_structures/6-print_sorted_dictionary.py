#!/usr/bin/python3
# a function that prints a dictionary by ordered keys.
# in only one set.
# set difference

def print_sorted_dictionary(a_dictionary):
    return dict(sorted(a_dictionary.items()))



print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
