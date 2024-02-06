#!/usr/bin/python3

"""provides functionality related to square"""


class Square:
    """class definition of square"""

    def __init__(self, size=0):
        """
        Initializes a new square.
        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character #.
        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
