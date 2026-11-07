#!/usr/bin/python3
"""
XML Serialization and Deserialization Module.

This module provides functionality to serialize a Python dictionary
into an XML file and deserialize an XML file back into a Python dictionary.
"""
import xml.etree.ElementTree as ET



def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    """Iterate through the dictionary items and
    add them as child elements."""
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    """Create an ElementTree object and write to the file."""
    tree = ET.ElementTree(root)
    tree.write(filename)
    
def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    """Create a dictionary to hold the deserialized data."""
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
