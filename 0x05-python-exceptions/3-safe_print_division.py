#!/usr/bin/python3

# function that divides two integers and
# prints the results

def safe_print_division(a, b):
    try:
        total = a / b
    except ZeroDivisionError:
        total = None
    finally:
        print("Inside result: {}".format(total))
        return(total)
