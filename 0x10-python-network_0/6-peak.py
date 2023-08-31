#!/usr/bin/python3
"""
unsorted list of integers, and you need to find a peak in the list.
"""


def find_peak(list_of_integers):
    """
    idea is to divide the list into two halves and compare
    the middle element with its neighbors
    """
    if len(list_of_integers) == 0:
        return
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    for i in range(0, len(list_of_integers)):
        if i == len(list_of_integers) - 1:
            if list_of_integers[i] > list_of_integers[i - 1]:
                return list_of_integers[i]
        elif list_of_integers[i] > list_of_integers[i + 1]\
                and list_of_integers[i] > list_of_integers[i - 1]:
            return list_of_integers[i]
    return list_of_integers[0]
