#!/usr/bin/python3

#  a function that returns a key with the biggest
#  integer value.
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxValue = 0
    maxKey = None
    for key, value in a_dictionary.items():
        if value > maxValue:
            maxValue = value
            maxKey = key
    return maxKey
