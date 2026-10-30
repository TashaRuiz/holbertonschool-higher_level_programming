#!/usr/bin/python3
"""Task said: Write an empty class BaseGeometry."""


class BaseGeometry:
    """creating empty class BaseGeometry"""
    def area(self):
        """raise error messege indicating area metod is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
