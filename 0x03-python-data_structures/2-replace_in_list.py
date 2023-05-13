#!/usr/bin/python3

# Function that replaces an element of alist at a specific position

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

# modifies elements at a specific index
    new_list = my_list
    new_list[idx] = element
    return new_list
