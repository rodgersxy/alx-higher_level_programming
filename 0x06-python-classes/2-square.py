#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """instatiation"""
    def __init__(self, size=0):
        """
        size - argument with dafault value 0
        __size - private instance attribute
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
