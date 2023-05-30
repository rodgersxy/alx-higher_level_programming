#!/usr/bin/python3
"""prototype"""


class Square:
    """instantiation
    __size - private instance attribute that will store
    size of the square
    """
    def __init__(self, size=0):
        """Raises: TypeError- exception if size
        is not an integer
        ValueError- exception if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area method to calculate
        area of square
        """
        return(self.__size**2)
