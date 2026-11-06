#!/usr/bin/python3
"""Module that reads a text file (UTF8) and prints it to stdout"""


class Student:
    """Class representing a student"""
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """Method that retrieves a dictionary representation of a Student instance"""
    def to_json(self):
        return self.__dict__
