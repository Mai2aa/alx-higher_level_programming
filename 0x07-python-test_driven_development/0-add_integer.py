#!/usr/bin/python3
""" integers addition
adds two integers
a and b
a + b
return the sum of a and b"""


def add_integer(a, b=98):
    """a function that adds two integers
    int: a
    int: b"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return result
