#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstract base class representing a generic shape.

    area: Abstract method to calculate the area of the shape.
    perimeter: Abstract method to calculate the perimeter of the shape.
    """
    @abstractmethod
    def area(self):
        """Calculate the area of the shape
        then return a float area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    class circle that inheriting from shape.
    initialize the circle instance with radius
    """
    def __init__(self, radius=0):
        if type(radius) in [int, float]:
            self.radius = abs(radius)

    def area(self):
        """Calculate the area of the shape
        then return a float area of the shape
        """
        return (pi * (self.radius ** 2))

    def perimeter(self):
        return (2 * pi * self.radius)

class Rectangle(Shape):
    """
        class rectangle that inheriting from shape.
        initialize the circle instance with 
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
        """
    def __init__(self, width=0, height=0):
        if type(width) in [int, float]:
            self.width = width

        if type(height) in [int, float]:
            self.width = height

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        return (2 * self.width) + (2 * self.height)

def shape_info(Shape):
    """Display the area and perimeter of the shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
