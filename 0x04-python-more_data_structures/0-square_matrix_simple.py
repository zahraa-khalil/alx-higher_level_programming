#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    multi = list(map(lambda arr: list(map(lambda x: x ** 2, arr)), matrix))

    print(multi)
