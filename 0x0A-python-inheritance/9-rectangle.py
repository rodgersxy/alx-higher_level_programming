#!/usr/bin/python3
"""imports the BaseGeometry class from the 7-base_geometry
module and assigns it to the BaseGeometry variable."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle that inherits from the BaseGeometry class.
    """
    def __init__(self, width, height):
        """
        takes two parameters
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        calculates and return the area of rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """prints"""
        return(f"[Rectangle] {self.__width}/{self.__height}")
