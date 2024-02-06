#!/usr/bin/python3

"""provides functionality related to square"""


class Square:
    """class definition of square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square.
        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        Raises:
            TypeError: If size is not an int
                or position is not a tuple of 2 +ve int.
            ValueError: If size is less than 0
                or position contains non +ve int.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Getter method for retrieving the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for setting the position of the square.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise ValueError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculates the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #.
        If size is equal to 0, prints an empty line.
        Position is used by adding leading spaces.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
