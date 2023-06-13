#!/usr/bin/python3
"""a function that returns the JSON representation
of an object (string)"""
import json


def to_json_string(my_obj):
    """
    to use json.dump() function to convert object to JSON
    """
    json_str = json.dumps(my_obj)
    return json_str
