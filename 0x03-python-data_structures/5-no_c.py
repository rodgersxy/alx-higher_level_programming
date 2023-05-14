#!/usr/bin/python3

# A prog that will remove all characters 'C' and 'c'
# from a string

def no_c(my_string):
    new_string = ""
    for string in (my_string):
        if string != 'C' and string != 'c':
            new_string += string

    return new_string
