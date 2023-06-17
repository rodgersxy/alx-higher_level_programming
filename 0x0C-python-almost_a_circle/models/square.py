#!/usr/bin/python3
"""
the class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class representing square that inherits from the
    Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initialize Square instances
        Args:
            size(int) - the size of the square
            x(int) - x coordinates(default=0)
            y(int) - y coordinates(default=0)
            id(int) - square identifier(default=None)
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        getter for size attribute
        returns width and height
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        setter for size attribute
        Validates the size using the same validation as width
        in Rectangle
        """
        self.data_validator("width", size)
        self.width = size
        self.height = size

    def __str__(self):
        """
        returns a string represantation of the sqaure
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """
        updating the attributes of square
        Args:
            *args - list of arguments
            **kwargs - key word arguments
        """
        args_list = ["id", "size", "x", "y", "\0"]
        if (len(args)):
            for i in range(len(args)):
                setattr(self, args_list[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        returns dictionary representation of the square
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }
