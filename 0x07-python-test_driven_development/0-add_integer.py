#!/usr/bin/python3
"""This Module is for add_integer method"""


def add_integer(a, b=98):
    """This function adds two integers.

    Args:
        a: integer number one
        b: integer number two, default value is 98.

    Raises:
        TypeError: if a, b are not int, float.

    Returns:
        The sum of integers
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")