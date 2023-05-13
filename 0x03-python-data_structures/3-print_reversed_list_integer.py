#!/usr/bin/python3

# function that prints all integers in a list in reverse order

def print_reversed_list_integer(my_list=[]):
    if type(my_list) is list:
        my_list.reverse()
        for num in my_list:
            print("{:d}".format(num))
