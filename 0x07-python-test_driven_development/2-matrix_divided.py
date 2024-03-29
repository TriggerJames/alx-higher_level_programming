#!/usr/bin/python3
"""This Module is matrix_divided Method"""


def matrix_divided(matrix, div):
    """Divide elemnts by divider
    matrix [[]]: this is a list of lists
    div (int): this an integer that doesn't equal zero.

    Returns: a whole new matrix
    """
    if not isinstance(matrix, list) or\
       not any(isinstance(matrix[0], list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    "matrix must be a matrix " +
                    "(list of lists) of integers/floats")
    for row in matrix:
        if len(row) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")