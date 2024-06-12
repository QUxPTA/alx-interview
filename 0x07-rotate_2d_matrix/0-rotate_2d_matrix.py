#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix by 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The n x n 2D matrix to be rotated.

    Returns:
        None: The matrix is modified in place.
    """
    # Step 1: Transpose the matrix
    transpose(matrix)
    # Step 2: Reverse each row
    reverse_rows(matrix)


def transpose(matrix):
    """
    Transposes the given n x n 2D matrix in place.
    """
    n = len(matrix)
    # Iterate over the matrix
    for i in range(n):
        for j in range(i + 1, n):
            # Swap elements at position (i, j) with (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_rows(matrix):
    """
    Reverses each row of the given n x n 2D matrix in place.
    """
    # Iterate through each row and reverse it
    for row in matrix:
        row.reverse()
