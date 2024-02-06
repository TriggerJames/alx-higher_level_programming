#!/usr/bin/python3

"""provides functionality related to square"""


class Square:
    """represents a square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
