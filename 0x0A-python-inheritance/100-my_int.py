#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """
    declares MyInt class that inherits int
    """
    def __init__(self, value):
        """
        initialise value passed and assyn to numbers
        """
        self.numbers = value

    def __eq__(self, num1):
        """
        overrides the __eq__() method to invert the behavior
        of the == operator
        """
        return self.numbers != num1

    def __ne__(self, num2):
        """
        overrides the __ne__() method to invert the behavior
        of the != operator
        """
        return self.numbers == num2
