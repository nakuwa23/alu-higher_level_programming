#!/usr/bin/python3
"""This module implements the Pascal's triangle"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the specified number of rows.

    Args:
        num_rows: The number of rows to generate in Pascal's Triangle.

    Returns:
        A list of lists representing Pascal's Triangle.
    """
    triangle = []

    for row_num in range(n):
        # Initialize the current row with 1s.
        # The length of row_num is row_num + 1.
        current_row = [1] * (row_num + 1)

        # Calculate the middle elements of the current row
        # by summing elements from the previous row.
        if row_num > 1:  # Only for rows beyond the first two
            for j in range(1, row_num):
                var_1 = triangle[row_num - 1][j - 1]
                var_2 = triangle[row_num - 1][j]
                current_row[j] = var_1 + var_2

        triangle.append(current_row)

    return triangle

if __name__ == "__main__":
    triangle = pascal_triangle(5)

    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
