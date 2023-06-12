#!/usr/bin/python3
"""a class Square that inherits from Rectangle (9-rectangle.py)"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    defines square class that inherits Rectangle
    """
    def __init__(self, size):
        """
        constructor method for Square that take in size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        returns string that represents square description
        """
        return(f"[Square] {self.__size}/{self.__size}")
