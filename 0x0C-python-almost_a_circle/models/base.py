#!/usr/bin/python3
"""
This module has a class will be the “base” of all other classes
in this project.
__nb_objects = 0  (private class attribute)
"""


class Base:
    """
    class 'Base' will be base of all other classes in the project
    Args:
        id(int)- id value for the instance, if provided assign it
        to public instance attr. If not provided, increment
        private class attr "__nb_objects" and assign new value to
        the public instance attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor for the Base
        id - instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
