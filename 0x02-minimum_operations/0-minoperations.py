#!/usr/bin/env python3
"""
Minimum operations
"""


def minOperations(n: int) -> int:
    """minimum operations to reduce n to 1"""
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return n
