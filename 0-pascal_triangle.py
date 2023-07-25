#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """Return a list of lists of integers representing the pascal's triangle of n

    Args:
        n (int): number of rows
    """
    if n <= 0:
        return []
    result = []

    for i in range(n):
        row = []
        # cols in row is i + 1
        for j in range(i + 1):
            # cell is at [row, cell]
            row.append(combination(i, j))
        result.append(row)

    return result


def combination(n, r):
    """Return the combination of a n and r (nCr)

    Args:
        n (int): total number of objects
        r (int): number of chosen objects
    """
    denominator = factorial(n - r) * factorial(r)
    return int(factorial(n) / denominator)


def factorial(n):
    """Return the factorial of a number

    Args:
        n (int): number
    """
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)
