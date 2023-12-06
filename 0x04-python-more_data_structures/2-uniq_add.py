#!/usr/bin/python3
# a function that adds all unique integers in a list (only once for each integer).
def uniq_add(my_list=[]):
    setArr = set(my_list)
    return sum(setArr)
