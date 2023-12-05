#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry:
    """define a class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater then 0".format(name))
        else:
            self.__value = value