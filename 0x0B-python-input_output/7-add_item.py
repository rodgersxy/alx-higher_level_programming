#!/usr/bin/python3
"""a script that adds all arguments to a Python list,
and then save them to a file"""


import sys
import json


from_file = __import__('6-load_from_json_file').load_from_json_file
to_file = __import__('5-save_to_json_file').save_to_json_file


"""variable holds the name of the JSON file to be loaded and saved"""
filename = "add_item.json"
try:
    my_list = from_file(filename)
except FileNotFoundError:
    my_list = []
finally:
    my_list.extend(str(arg) for arg in sys.argv[1:])
    to_file(my_list, filename)
