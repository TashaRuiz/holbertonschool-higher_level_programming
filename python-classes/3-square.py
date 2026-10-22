#!/usr/bin/python3
"""class Square that defines a square based on 1-square.py"""


class Square:
    def __init__(self, size=0):
        """Init a square with size validation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
