#!/usr/bin/python3
"""
Island Perimter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island described in grid.

    Args:
        grid (list of list of int):
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # This is a land cell
                # Check top cell
                if row == 0 or grid[row-1][col] == 0:
                    perimeter += 1

                # Check bottom cell
                if row == rows - 1 or grid[row+1][col] == 0:
                    perimeter += 1

                # Check left cell
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1

                # Check right cell
                if col == cols - 1 or grid[row][col+1] == 0:
                    perimeter += 1

    return perimeter
