#!/usr/bin/python3
"""
Minimum Operations module
"""


def minOperations(n):
    """
    Calculates the fewest number of operations (Copy All / Paste)
    needed to result in exactly n H characters in the file.

    The answer is the sum of the prime factors of n.
    Returns 0 if n is impossible to achieve.
    """
    if not isinstance(n, int) or n < 2:
        return 0

    ops = 0
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            ops += factor
            n //= factor
        factor += 1
    if n > 1:
        ops += n
    return ops
