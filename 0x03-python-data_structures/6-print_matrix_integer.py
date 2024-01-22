#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elements in row:
            print("{:d}".format(elements), end="")
            if (elements != row[len(row)-1]):
                print(" ", end="")
        print()
