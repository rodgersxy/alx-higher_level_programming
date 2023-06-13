#!/usr/bin/python3
"""from Class to JSON"""


def class_to_json(obj):
    """
    class_to_json function simply returns the
    __dict__ attribute of the object
    """
    return obj.__dict__
