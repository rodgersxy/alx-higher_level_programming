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
        self.data_validator("width", width)
        self.__width = width

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
        self.data_validator("height", height)
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
        self.data_validator("x", x)
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
        self.data_validator("y", y)
        self.__y = y

    def data_validator(self, name, value):
        """
        validates and checking of type and values of arguments
        before assigning value to corresponding private attri
        Args:
            name(str) : name of arguments
            value : value of the the argument
        Raises:
            TypeError:  If the input is not an integer
            ValueError: If the values are not within the allowed
            range
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        else:
            if (name in ["width", "height"] and value <= 0):
                raise ValueError("{} must be > 0".format(name))
            elif (name in ["x", "y"] and value < 0):
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """
        public method that returns the area of the
        rectangle
        """
        return self.width * self.height

    def display(self):
        """
        adding the public method def display(self)
        that prints in stdout the Rectangle instance with the
        character #
        """
        for i in range(self.y):
            print("\n", end="")
        for j in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for m in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        overriding the __str__ method so that it returns [Rectangle]
        elements
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        update method to update attrributes of the rectangle
        that accepts *args and **kwargs
        """
        args_list = ["id", "width", "height", "x", "y", "\0"]
        if (len(args)):
            for i in range(len(args)):
                setattr(self, args_list[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        to_dictionary method is used to return a dictionary
        representation of a rectangle object
        """
        return {
            attr: getattr(self, attr)
            for attr in ['id', 'width', 'height', 'x', 'y']
            }
