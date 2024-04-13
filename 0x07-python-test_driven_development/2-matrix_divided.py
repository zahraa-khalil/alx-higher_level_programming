#!/usr/bin/python3
"""Module add integer"""


def matrix_divided(matrix, div):
    """divide elemets of matrix
    Args: 
        matrix: a list of lists of integers or floats,
        div: a number (integer or float)

    Raises:
        TypeError: if matrix isn't a list of lists of integers or floats,
        or div is not a number (integer or float)

    Returns: 
        a new matrix
    """

    if type(div) not in (int, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    if isinstance(matrix, list) or len(matrix) > 0:
        length = len(matrix[0])
        for element in matrix:
            if not isinstance(element, list) or len(element) == 0:
                raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/floats')
            if len(element) != length:
                raise TypeError(
                    'Each row of the matrix must have the same size')
            for i in element:
                if not isinstance(i, (int, float)):
                    raise TypeError(
                        'matrix must be a matrix (list of lists) of integers/floats')
                else:
                    element[i] = round(element / div, 2)
                    return matrix
    else:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    return [[round(x/div, 2) for x in row] for row in matrix]


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
