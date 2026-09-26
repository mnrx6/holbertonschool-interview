#!/usr/bin/python3
"""Pascal's Triangle module."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]

        for num in range(i - 1):
            row.append(triangle[-1][num] + triangle[-1][num + 1])

        if i != 0:
            row.append(1)

        triangle.append(row)

    return triangle
