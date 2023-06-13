#!/usr/bin/python3
"""
a function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Open the file in write mode"""
    with open(filename, "w", encoding="utf-8") as f:
        """write text to the file"""
        counter = f.write(text)
    return counter
