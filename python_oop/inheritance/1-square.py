#!/usr/bin/env python3
"""Module defining the Square class."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """A square defined by its size, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialise a Square instance.

        Args:
            size (int): The side length of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
