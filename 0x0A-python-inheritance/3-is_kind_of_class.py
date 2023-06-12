#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """"
    Returns True is the object is an instantance of
    or if the object is an instance of a class that is
    inherited from(specific class) otherwise False.
    Args:
        obj - any object, a_class - class object
    """
    return isinstance(obj, a_class)
