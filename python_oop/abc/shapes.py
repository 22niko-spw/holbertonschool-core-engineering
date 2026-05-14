#!/usr/bin/env python3
"""Abstract Shape class, concrete subclasses, and shape_info function."""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        ...

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        ...


class Circle(Shape):
    """A circle defined by its radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """A rectangle defined by its width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of any shape-like object (duck typing)."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
