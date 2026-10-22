#!/usr/bin/python3
"""class Square that defines a square based on 1,2,3-square.py"""


class Square:
    """ attributes for __size(int)"""

    def __init__(self, size=0):
        """Initializes a Square instance with size validation"""
        self.size = size

    def area(self):
        """Calculates and return the area value of square"""
        return self.__size ** 2

    @property
    def size(self):
        """Gather for the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
