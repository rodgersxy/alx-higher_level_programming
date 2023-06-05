#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """
    __init__ method that initializes Rectangle
    object with width and height parameters
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter method to retrieve value of
        width attribute
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        setter method to set the value of width attr
        performs validation
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """
        getter method to retrieve value of the
        height attribute
        """
        return self.__height

    @height.setter
    def height(self, height):
        """heght of the rectangle"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """method to calculate area of rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """calculate the perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))
