#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry:
    """define a class"""
    def area(self):
        """define area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """define a validator fuction"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
