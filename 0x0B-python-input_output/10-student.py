#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:

    def __init__(self, first_name, last_name, age):
        """
        Student class has three public instance attributes:
        first_name, last_name, and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json method to retrieve dict
        """
        if type(attrs) is list:
            return {x: self.__dict__.get(x)
                    for x in attrs if x in self.__dict__}
        return self.__dict__
