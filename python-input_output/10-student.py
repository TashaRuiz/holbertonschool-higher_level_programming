#!/bin/usr/python3
"""Module that reads a text file (UTF8) and prints it to stdout"""

class Student:
    """Class representing a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a 'dictionary' representation
        of a Student instance"""
        if attrs is None:
            return self.__dict__
        
        else:
            return {key: value for key, 
                    value in self.__dict__.items() if key in attrs}
