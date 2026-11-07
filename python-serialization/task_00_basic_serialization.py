#!/usr/bin/python3
"""Basic serialization module from Python to JSON"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python object to JSON and saves it to a file.

    Args:
        data: The Python object to serialize.
        filename: The name of the file to save the JSON data to.
    """
    with open(filename, 'w', encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile)

def load_and_deserialize(filename):
    """Loads JSON data from a file and deserializes it to a Python object.

    Args:
        filename: The name of the file to load the JSON data from."""
    with open(filename, r, encoding="utf-8") as jsonfile:
        return json.load(jsonfile)
