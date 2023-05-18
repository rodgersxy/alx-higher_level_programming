#!/usr/bin/python3

# function that returns the weighted average of all integers tuple

def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0

    total_weight = 0
    total_score = 0

    for x, y in my_list:
        total_weight += x * y
        total_score += y
    return (total_weight / total_score)
