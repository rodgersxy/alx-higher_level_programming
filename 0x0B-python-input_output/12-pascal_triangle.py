#!/usr/bin/python3
""" function def pascal_triangle(n): that returns a list of
lists of integers representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """
    pascal triangle
    n - number of iteration
    """
    triangle = []

    for i in range(n):
        row = []
        for x in range(i + 1):
            if x == 0 or x == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][x - 1] + triangle[i - 1][x])
        triangle.append(row)

    return triangle
