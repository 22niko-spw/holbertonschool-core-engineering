#!/usr/bin/env python3
"""Module defining the Rectangle class."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle defined by its width and height."""

    def __init__(self, width, height):
        """Initialise a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
