#!/usr/bin/python3

# deletes a key in the dictionary

def simple_delete(a_dictionary, key=""):

    if key in a_dictionary:
        a_dictionary.pop(key)

    return (a_dictionary.copy())
