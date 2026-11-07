#!/usr/bin/python3
"""Basic serialization module from Python to JSON"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python object to JSON and saves it to a file.

    Args:
        data: The Python object to serialize.
        filename: The name of the file to save the JSON data to.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)
