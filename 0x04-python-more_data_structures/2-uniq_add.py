#!/usr/bin/python3

# a function that adds all unique integers in a list
# those that appears only once

def uniq_add(my_list=[]):
    total = sum(set(my_list))

    return total
