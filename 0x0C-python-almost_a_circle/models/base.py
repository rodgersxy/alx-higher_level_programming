#!/usr/bin/python3
"""
This module has a class will be the “base” of all other classes
in this project.
__nb_objects = 0  (private class attribute)
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns JSON string of list_dictionaries
        Args:
            list_dictionaries (list): List of dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            json_str = "["
            for elt in list_dictionaries:
                json_str += json.dumps(elt)
                json_str += ", "
            json_str = json_str[:-2] + "]"
        return json_str

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list represented by the JSON string json_string
        Args:
            json_string (str): JSON string representing a list
            of dictionaries
        Returns -list represented by JSON
        """
        if json_string is None or len(json_string) == 0:
            return list()
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs
        to a file
        Args:
            list_objs (list): List of instances inheriting
            from Base.
        """
        filename = cls.__name__+".json"
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                file.write(cls.to_json_string(
                    [elt.to_dictionary() for elt in list_objs]))
