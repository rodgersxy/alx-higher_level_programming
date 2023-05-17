#!/usr/bin/python3

# a function that replaces all occurance of an
# element by another in a new list

def search_replace(my_list, search, replace):
    # my_list is the initial list
    new_list = []
    for items in my_list:
        if items == search:
            new_list.append(replace)
        else:
            new_list.append(items)

    return new_list
