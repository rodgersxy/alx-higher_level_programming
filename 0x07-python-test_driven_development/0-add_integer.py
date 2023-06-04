#!/usr/bin/python3
"""Fuction that adds two integers"""


def add_integer(a, b=98):
    """
    adding two integers, return a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a + b)
