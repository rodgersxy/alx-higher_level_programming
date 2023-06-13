#!/usr/bin/python3
""" a function that appends a string at the end of a text file
(UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """
    open file in append mode
    """
    with open(filename, "a", encoding="utf-8") as f:
        """write text to the file and store in variable counter"""
        counter = f.write(text)
    return counter
