#!/usr/bin/python3
"""class Rectangle for String representation"""


class Rectangle:
    """defines a class named Rectangle"""
    def __init__(self, width=0, height=0):
        """
        initializes a new instance with width and
        height parameters
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter method allow accessing of private
        instance attribute
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        setting the value of private instance attribute
        and validation
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """
        height of rectangle and validation
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """
        calculate the area and return the area
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        calculates and return the perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """
        string representation method
        returns string that represents the rectangle using #
        """
        rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return rectangle
        for x in range(self.__height):
            for y in range(self.__width):
                rectangle += "#"
            if x < self.__height - 1:
                rectangle += "\n"
        return rectangle
