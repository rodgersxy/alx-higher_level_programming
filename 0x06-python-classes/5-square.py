#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """defines a class named Square"""
    def __init__(self, size=0):
        """
        __init__ - a constructor method of Square class
        (size=0)- optional parameter that defaults to 0
        __size -initialize private instance attribute
        with 'size' value
        """
        self.__size = size

    @property
    def size(self):
        """
        property decorater to define getter method of
        'size' attribute, returns the value of private
        attribute '__size'
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        property setter method of 'size' attribute
        checks if provided attributes are integers
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        this method calculates the area of the square
        multiplies the value of '__size' attribute
        """
        return self.__size ** 2

    def my_print(self):
        """
        To print in stdout the square using '#'
        character
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.size):
                for x in range(self.size):
                    print('#', end='')
                print()
