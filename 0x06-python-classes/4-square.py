#!/usr/bin/python3
"""Class Square that defines a sqaure"""


class Square:
    """
    instantiation of size
    with __init__ method
    """
    def __init__(self, size=0):
        """__size: private instance attribute
        to store size square
        """
        self.__size = size

    @property
    def size(self):
        """
        the getter method for retriving value
        of __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter method to check if value
        is integer
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        area method
        calculating area of the square
        """
        return self.__size ** 2
