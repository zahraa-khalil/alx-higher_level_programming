#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for i, x in enumerate(my_list):
        if x % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False

    return new_list
