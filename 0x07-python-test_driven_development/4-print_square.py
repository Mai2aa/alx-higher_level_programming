#!/usr/bin/python3
"""print square"""


def print_square(size):
    """print a square"""
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
