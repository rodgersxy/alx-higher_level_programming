#!/usr/bin/python3

def uppercase(str):
    for char in str:
        # If in lowercase covert to uppercase
        if (ord(char) >= 97 and ord(char) <= 122):
            uppercase_char = ord(char) - 32
        else:
            # Else leave it like that
            uppercase_char = ord(char)
        print("{:c}".format(uppercase_char), end="")

    print()
