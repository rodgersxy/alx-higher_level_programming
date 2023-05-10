#!/usr/bin/python3

# Returns True is c is lowercase else False

def isLower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
