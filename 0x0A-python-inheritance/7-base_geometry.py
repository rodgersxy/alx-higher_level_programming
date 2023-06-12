#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry:
    """
    Base class that doesn't have attribute or method
    """

    def area(self):
        """
        computes the area of geometry
        Raise: Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        public instance method that validates the intger input
        Raise: TypeError - If the value is not an integer
        ValueError - If the value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
