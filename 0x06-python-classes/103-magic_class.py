#!/usr/bin/python3
"""ByteCode -> Python"""
import math


class MagicClass:
    """define a class"""
    def __init__(self, radius=0):
        if not isinstance(radius, int) or not isinstance(radius, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return math.pi * 2 * self.__radius
