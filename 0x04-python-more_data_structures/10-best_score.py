#!/usr/bin/python3

# program that returns a key with the biggest integer value

def best_score(a_dictionary):
    max_key = 0

    if not a_dictionary:
        return "None"

    for idx in a_dictionary:
        if a_dictionary[idx] > max_key:
            max_key = a_dictionary[idx]

            name = idx
    return name
