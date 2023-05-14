#!/usr/bin/python3

# a program that replaces elements in a list at a specific
# position without modifying original list

def new_in_list(my_list, idx, element):
    if idx >= len(my_list) or idx < 0:
        return (my_list)
    new_list = my_list.copy()
    new_list[idx] = element

    return (new_list)
