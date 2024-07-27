#!/usr/bin/python3
"""
 Pascals Triangle Implementation
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
    n (int): The number of rows to generate.
    Must be a non-negative integer.

    Returns:
    list of lists: A list of lists where each inner list represents
                        a row in Pascal's Triangle.
                Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if i == 0:
            # The first row is always [1]
            row = [1]
        else:
            row = []
            # Get the previous row from the triangle
            prev_row = triangle[i - 1]
            # The first element of the row is always 1
            row.append(1)
            # Each element (except the first and last) is the sum of
            # the two elements above it
            for j in range(1, len(prev_row)):
                row.append(prev_row[j - 1] + prev_row[j])
            # The last element of the row is always 1
            row.append(1)

        # Add the current row to the triangle
        triangle.append(row)

    return triangle
