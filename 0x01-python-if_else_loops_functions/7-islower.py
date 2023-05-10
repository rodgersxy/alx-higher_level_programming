#!/usr/bin/python3

# Returns True is c is lowercase else False

def isLower(c):
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False
