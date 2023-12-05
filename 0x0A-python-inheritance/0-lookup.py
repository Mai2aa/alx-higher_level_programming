#!/usr/bin/python3
""" task 0"""


def lookup(obj):
    """ a function that returns a list of available attributes
    and methods of an object"""
    return list(dir(obj))