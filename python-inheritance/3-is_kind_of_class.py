#!/usr/bin/python3
"""Checks function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class; otherwise False."""


def is_kind_of_class(obj, a_class):
    """Checking if an obj is an instance
    or an instance of an inherited a_class from."""
    if isinstance(obj, a_class):
        return True
    return False
