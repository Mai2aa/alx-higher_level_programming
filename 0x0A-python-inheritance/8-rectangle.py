#!/usr/bin/python3
"""Rectangle"""
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
        super()

class Rectangle(BaseGeometry):
    """define a class"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        Rectangle.integer_validator
        