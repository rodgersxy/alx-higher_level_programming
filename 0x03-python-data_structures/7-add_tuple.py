#!/usr/bin/python3

# Function that adds two tuples
# tuple_a: first tuple
# tuple_b: second tuple

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a += 0, 0
    if len(tuple_b) < 2:
        tuple_b += 0, 0

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
