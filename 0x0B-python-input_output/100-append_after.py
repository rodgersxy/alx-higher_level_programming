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
    with open(filename, "r") as f:
        lines = f.readline()

    content = []

    for i in range(len(lines)):
        content.append(lines[i])
        if search_string in lines[i]:
            content.append(new_string)

    with open(filename, "w") as f:
        f.write("".join(content))
