#!/usr/bin/python3
"""magic string"""


def magic_string():
    iteration = magic_string.iteration if hasattr(magic_string, 'iteration') else 0
    magic_string.iteration = iteration + 1
    return "BestSchool" * magic_string.iteration
