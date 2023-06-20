#!/usr/bin/python3
"""
This module has a class will be the “base” of all other classes
in this project.
__nb_objects = 0  (private class attribute)
"""
import json
import csv
import turtle


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

    @classmethod
    def create(cls, **dictionary):
        """
        returns instance with all attributes
        Args:
            **dictionary: Double pointer to a dictionary
        Returns - Base: instance with all attri
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        else:
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        Args:
            list of instance
        """
        filename = cls.__name__ + ".json"
        instance_result = []
        try:
            with open(filename, "r", encoding="utf-8") as file:
                read_file = file.read()
            instance_list = cls.from_json_string(read_file)
            for elt in instance_list:
                instance_result.append(cls.create(**elt))
            return instance_result
        except Exception:
            return instance_result

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        to write the csv file of the object lists
        Args:
            list_objs - object list
        """
        filename = cls.__name__+".csv"
        if cls.__name__ == "Rectangle":
            labels = ["id", "width", "height", "x", "y"]
        else:
            labels = ["id", "size", "x", "y"]
        list_of_dict = [elt.to_dictionary() for elt in list_objs]
        with open(filename, "w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=labels)
            writer.writeheader()
            for elt in list_of_dict:
                writer.writerow(elt)

    @classmethod
    def load_from_file_csv(cls):
        """
        returning lists of instances
        """
        filename = cls.__name__+".csv"
        list_instance = []
        list_result = []
        try:
            with open(filename) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    for field_name in row:
                        row[field_name] = int(row[field_name])
                    list_instance.append(row)
                for dic in list_instance:
                    list_result.append(cls.create(**dic))
            return list_result
        except Exception:
            return list_result

    def draw(list_rectangles, list_squares):
        """
        opens a window and draws all the Rectangles and Squares
        Args:
            list_rectangles: list of rectangle
            list_square: list of square
        """
        turtle.speed(0)
        screen = turtle.Screen()

        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.color(random.choice(['red', 'green', 'blue']))
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.left(90)
                turtle.forward(rectangle.height)
                turtle.left(90)
            turtle.end_fill()

        # Create a turtle for each square

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.color(random.choice(['red', 'green', 'blue']))
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)
            turtle.end_fill()

        turtle.done()
