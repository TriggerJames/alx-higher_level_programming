#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dic = {x: value * 2 for x, value in a_dictionary.items()}
    return new_dic
