#!/usr/bin/python3
""" integers addition"""


def add_integer(a, b=98):
    """a function that adds two integers """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return result

if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")