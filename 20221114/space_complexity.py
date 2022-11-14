"""
Space Complexity
for loop: O(1)
reduce: O(3)
recursive: O(n)
"""


def factorial_for_loop(n: int) -> int:
    if n == 0:
        return 1
    fac = 1
    for idx in range(2, n + 1):
        fac *= idx
    return fac


def factorial_reduce(n: int) -> int:
    from functools import reduce

    if n == 0:
        return 1
    fac = reduce(lambda x, y: x * y, range(1, n + 1))
    return fac


def factorial_recursive(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
