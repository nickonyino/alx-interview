#!/usr/bin/python3
"""
Minimum Operations
Given a number n, writes a method calculating the fewest number of operations
needed to result in exactly n H characters in a specific file
Prototype: def minOperations(n)
Returns an integer
if n is impossible to achieve, return 0
"""


def minOperations(n):
    """
    Function minOperations
    Returns an integer
    """
    result = 0
    x = 2
    while n > 1:
        while n % x == 0:
            result += x
            n /= x
        x += 1
    return result
