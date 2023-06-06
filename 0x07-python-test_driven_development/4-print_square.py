#!/usr/bin/python3
"""function that prints square with the character #"""


def print_square(size):
    """
    takes a single parameter
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
