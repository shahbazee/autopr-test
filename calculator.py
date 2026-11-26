"""
Simple calculator module providing an add function.
"""

import numbers


def add(a, b):
    """
    Return the sum of a and b.
    Raises TypeError if either argument is not a numeric type.
    """
    if not isinstance(a, numbers.Number) or not isinstance(b, numbers.Number):
        raise TypeError("Both arguments must be numeric")
    return a + b
