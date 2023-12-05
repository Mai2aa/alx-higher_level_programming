#!/usr/bin/python3
"""print square instance"""


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
        if self.__size == 0:
            print()
            return
        else:
            lines = []
            for i in range(self.__position[1]):
                lines.append("\n")
            for j in range(self.__size):
                lines.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(lines)