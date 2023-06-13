#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """defines a function read_file that takes an optional filename"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
