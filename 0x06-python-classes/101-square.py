#!/usr/bin/python2
"""print square instance"""


from ast import pattern


class Square:
    """ define a class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not (isinstance(value, tuple)) or len(value) != 2
           or not all(isinstance(num, int) for num in value) or
           not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def __str__(self):
        if self.size == 0:
            return ""
        square_str = ''
        for i in range(self.position[1]):
            square_str += "\n"
        for j in range(self.size):
            square_str += " " * self.position[0] + "#" * self.size + "\n"
        return square_str.rstrip()
