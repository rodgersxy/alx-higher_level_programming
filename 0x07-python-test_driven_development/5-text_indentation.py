#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
    Print the text with 2 new lines after each
    of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    leading_whitespace = False
    index = 0
    while index < len(text):
        char = text[index]
        if char in ['.', '?', ':']:
            print(char, end="")
            print('\n')
            leading_whitespace = True
        else:
            if not leading_whitespace:
                print(char, end="")
            elif leading_whitespace and char == ' ':
                index += 1
                continue
            else:
                print(char, end="")
                leading_whitespace = False
        index += 1
