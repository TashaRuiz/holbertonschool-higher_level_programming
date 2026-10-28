#!/usr/bin/python3
"""
This module contains a single function `lookup` that retrieves a list of
available attributes and methods of an object.
"""


def lookup(obj):
    """
    Args:
        obj (any): The object to inspect.
        Returns the list of available attributes and methods of an object.
    Returns:
        A list of attributes and methods available for the given object.
    """
    return dir(obj)
