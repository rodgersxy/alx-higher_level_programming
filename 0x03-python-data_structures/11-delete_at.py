#!/usr/bin/python3


# Deletes elements from a list on a given index

def delete_at(my_list=[], idx=0):

    if idx < 0 or idx >= len(my_list):
        return (my_list)

    del my_list[idx]

    return (my_list)
