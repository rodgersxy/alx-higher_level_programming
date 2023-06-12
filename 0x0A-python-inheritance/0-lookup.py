#!/usr/bin/python3
"""function that returns a list of available attributes and
methods of an object"""


def lookup(obj):
    """
    Returns a list of attribute and methods of an object
    Args:
        obj - an object to inspect
    """
    return dir(obj)
