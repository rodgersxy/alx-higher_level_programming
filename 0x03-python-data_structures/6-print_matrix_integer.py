#!/usr/bin/python3

# a program that prints a matrix of integers

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join(str.format("{:d}", i) for i in row))
