#!/usr/bin/python3
"""function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    divides all matrix elements
    Args - matrix, div
    Raises:
        TypeError - div must be a number
        TypeError - Each row of the matrix must have the same size
        TypeError - matrix must be a matrix (list of lists) of
        integers/floats
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    if type(matrix[0]) == list and len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if all(isinstance(x, list) for x in matrix):
        for x in range(len(matrix)):
            if len(matrix[0]) != len(matrix[x]):
                raise TypeError("Each row of the matrix must have" +
                                " the same size")
        new_matrix = list(map(list, matrix))
        for y in range(len(new_matrix)):
            for x in range(len(new_matrix[0])):
                if type(new_matrix[y][x]) != int:
                    raise TypeError("matrix must be a matrix " +
                                    "(list of lists) of integers/floats")
                new_matrix[y][x] = float("{:.2f}".format(
                                    new_matrix[y][x] / div))
        return(new_matrix)
    else:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
