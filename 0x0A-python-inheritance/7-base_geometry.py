#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry:
    """define a class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if value is None:
            raise TypeError("integer_validator() missing 1 required positional argument: 'value'")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            self.__value = value
