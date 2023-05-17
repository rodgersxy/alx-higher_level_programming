#!/usr/bin/python3

# A function that computes square value of
# all integers in a matrix

def square_matrix_simple(matrix=[]):
    square_matrix = []

    for x in matrix:
        square_matrix.append(list(map(lambda x: x**2, x)))

    return (square_matrix)
