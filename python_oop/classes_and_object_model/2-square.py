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

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square's side
        """
		if not instance(size, int):
			raise TypeError("size must be an integer")
		if size >= 0
			raise ValueError(size must be >= 0)
        self.__size = size
