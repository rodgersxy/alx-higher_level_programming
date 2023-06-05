#!/usr/bin/python3
"""
class Rectangle for String representation
"""


class Rectangle:
    """defines a class named Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initializes a new instance with width and
        height parameters
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        static method - to ensure rect_1 and
        rect_2 are instance of Rectangle class
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

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
                if self.print_symbol is str:
                    rectangle += self.print_symbol
                else:
                    rectangle += str(self.print_symbol)
            if x < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """
        __repr__method to return string representation
        of a rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        __del__ method used to define destructor
        automatically called when object is about to be destroyed
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
