#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """defines class named Square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        __init__ : called when new instance is created.
        self,position - optional parameters.
        self.size,self.position - instance attributes
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        property decorator that defines getter method
        of 'size' attribute and returns private attribute
        '__size'
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        property setter method for size attribute
        resposible for setting the value of __size
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        property decorator that define getter method for
        'position' attribute.
        returns - the value of private attribute __position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        property setter method of 'position' attribute -
        checks and ensure value are in tuples of two
        positive integers
        TypeError - when it fails else assign '__position'
        a privte attribute
        """
        if isinstance(value, tuple) is False or len(value) != 2 \
           or isinstance(value[0], int) is False or value[0] < 0 \
           or isinstance(value[1], int) is False or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates return area of a sqaure
        """
        return(self.__self ** 2)

    def my_print(self):
        """
        prints the square using '#' character
        if '0' prints empty line and returns
        """
        if self.__size == 0:
            print()
            return
        for x in range(self.__position[1]):
            print()

        for x in range(self.__size):
            for y in range(0, self.__position[0]):
                print(" ", end="")
            for z in range(0, self.__size):
                print("#", end="")

            print()
