#!/usr/bin/python3

# import functions from module calculator_1.py

if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul

    # assign variables
    a = 10
    b = 5
    # prints results with formatted string
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
