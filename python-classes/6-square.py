#!/usr/bin/python3
"""class Square that defines a square based on 1,2,3-square.py"""


class Square:
    """ attributes for __size(int) The size of the square's sides (must be >= 0)
        attributes for __position (tuple) The position of the square
        (tuple of 2 positive integers)
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance with size validation"""
        self.size = size
        self.position = position

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
    
    @property
    def position(self):
        """Getter for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value,tuple) or len(value) != 2:
            raise TypeError('error')
        if not all(isinstance(num,int) and num >= 0 for num in value):
            raise TypeError('error')
        self.__position = value

    def area(self):
        """Calculates and return the area value of square"""
        return self.__size ** 2

    def my_print(self):
        """Prints a square using the '#' character based on its size"""
        if self.__size == 0:
            print()
            return
        else:
            for _ in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
