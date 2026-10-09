#!/usr/bin/python3
"""Minimum Operations module."""


def minOperations(n):

    operations = 0
    factor = 2

    while n > 1:
        """Return the minimum number of operations to reach n characters."""
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1

    return operations
