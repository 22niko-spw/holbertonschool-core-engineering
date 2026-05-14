#!/usr/bin/env python3
"""
Square module with position
"""


class Square:
    """A class representing a square with position"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        msg = "position must be a tuple of 2 positive integers"

        if type(value) is not tuple:
            raise TypeError(msg)
        if len(value) != 2:
            raise TypeError(msg)
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError(msg)
        if value[0] < 0 or value[1] < 0:
            raise TypeError(msg)

        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            spaces = self.__position[0]
            lines_before = self.__position[1]

            for line in range(lines_before):
                print()

            for line in range(self.__size):
                print(" " * spaces + "#" * self.__size)

    def __str__(self):
        if self.__size == 0:
            return ""

        result = ""
        spaces = self.__position[0]
        lines_before = self.__position[1]

        for line in range(lines_before):
            result = result + "\n"

        for line in range(self.__size):
            result = result + " " * spaces + "#" * self.__size
            if line < self.__size - 1:
                result = result + "\n"

        return result
