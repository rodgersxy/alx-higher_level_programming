#!/usr/bin/python3
"""Say my name"""


def say_my_name(first_name, last_name=""):
    """
    Arguments - takes two parameters,first_name
    and last_name(optional) with default ""
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        full_name = f"{first_name} {last_name}"
    else:
        full_name = first_name
    print(f"My name is {full_name.strip()}")
