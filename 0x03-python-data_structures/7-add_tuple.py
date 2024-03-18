#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) == 0):
        tuple_a = (0, 0)
    elif (len(tuple_a) == 1):
        tuple_a = (tuple_a[0], 0)
    if (len(tuple_b) == 0):
        tuple_b = (0, 0)
    elif (len(tuple_b) == 1):
        tuple_b = (tuple_b[0], 0)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])


# def add_tuple(tuple_a=(), tuple_b=()):
#     if len(tuple_a) >= 2 and len(tuple_b) >= 2:
#         element1 = tuple_a[0] + tuple_b[0]
#         element2 = tuple_a[1] + tuple_b[1]
#         new_tuple = (element1, element2)
#         return new_tuple
#     elif len(tuple_b) == 1:
#         element1 = tuple_a[0] + tuple_b[0]
#         element2 = tuple_a[1] + 0
#         new_tuple = (element1, element2)
#         return new_tuple
#     elif len(tuple_b) == 0:
#         new_tuple = (tuple_a[0], tuple_a[1])
#         return new_tuple
#     elif len(tuple_a) == 1:
#         element1 = tuple_a[0] + tuple_b[0]
#         element2 = 0 + tuple_b[1]
#         new_tuple = (element1, element2)
#         return new_tuple
#     elif len(tuple_a) == 0:
#         new_tuple = (tuple_b[0], tuple_b[1])
#         return new_tuple
