#!/usr/bin/python3

# prints multiples of 2 in a list

def divisible_by_2(my_list=[]):
    # create new list to store results
    result = []

    for number in my_list:
        if number % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    return result
