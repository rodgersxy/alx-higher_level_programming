#!/usr/bin/python3
"""
Write the class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Class constructor for Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width(int) - width of the rectangle
            height(int) - height of the rectangle
            x (int) - x-coordinates(default=0)
            y (int) - y-coorditates(default=0)
            id (int) - value for the instance: if not provided the
            super call will use logic of __init__ of 'Base class'
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        @property decorator is used to define getter methods for
        the private instance attributes
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        setter for width attribute
        sets the value of width
        """
        self._width = width

    @property
    def height(self):
        """
        height value
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        sets the value of height
        """
        self.__height = height

    @property
    def x(self):
        """
        returns the value of x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        sets the value of x
        """
        self.__x = x

    @property
    def y(self):
        """
        returns the value of y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        sets the value of the y
        """
        self.__y = y
