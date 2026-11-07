#!/usr/bin/python3
"""
This module defines a CustomObject class for demonstrating
basic serialization and deserialization using Python's pickle module.

The pickle module is used to serialize (save) and deserialize (load)
instances of the CustomObject class to/from files.
"""
import pickle


class CustomObject:
    """
    A custom class representing an object with attributes for name,
    age, and student status.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): A boolean representing if the person is a student.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the object to a file using pickle."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes the object from a file using pickle."""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
