#!/usr/bin/python3
"""Module that reads a text file (UTF8) and prints it to stdout"""


def class_to_json(obj):
    """Return the dictionary description with simple 
    data structure (list, dictionary, string, integer 
    and boolean) for JSON serialization"""
    return obj.__dict__
