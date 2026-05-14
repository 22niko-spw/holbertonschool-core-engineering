#!/usr/bin/env python3
"""
Square module - defines a Square class with size attribute
"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square (private)
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square's side
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#"*self.__size)
