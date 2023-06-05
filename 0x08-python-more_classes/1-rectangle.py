#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle:
    """defination of class named Rectangle"""
    def __init__(self, width=0, height=0):
        """
        constructor method __init__ for Rectangle class
        initializes instance attribute width and height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        use to define getter method for width
        attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for width attribute
        resposible for validating input values and
        setting value of private attr __width
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """
        to define getter method for height attribute
        to allow access of value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for height attribute
        if value id none integer 'TypeError' is raise
        raise ValueError when value < 0
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
