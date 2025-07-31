#!/usr/bin/python3
"""
This module divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix

    Args:
        matrix (2d array of int or float)
            list of lists of integers or floats
        div (int or float): divisor

    Returns:
        a new matrix of the quotients
    """
    new_list = []

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        inner_list = []
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int\
               and type(matrix[i][j]) is not float:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            if len(matrix[0]) != len(matrix[i]):
                raise TypeError("Each row of the matrix"
                                " must have the same size")
            inner_list.append(round((matrix[i][j]) / div, 2))
        new_list.append(inner_list)
    return new_list
