#!/usr/bin/python3
"""a class BaseGeometry"""


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
