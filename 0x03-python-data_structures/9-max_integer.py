#!/usr/bin/python3

# Find the biggest integer in a list

def max_integer(my_list=[]):
    if not my_list:
        return None

    biggest_int = my_list[0]

    for integer in my_list[1:]:
        if integer > biggest_int:
            biggest_int = integer

    return biggest_int
