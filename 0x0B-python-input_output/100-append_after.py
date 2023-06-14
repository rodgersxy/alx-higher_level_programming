#!/usr/bin/python3
"""a function that inserts a line of text to a file
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a
    specific string in a file.
    arguments:
    filename(str) - file name
    search_string(str) - specifies each string to search for in
    each line
    new_string - the line of text to insert
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    content = []

    for line in lines:
        content.append(line)
        if search_string in line:
            content.append(new_string + '\n')

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(content)
