#!/usr/bin/python3
"""Module that reads a text file (UTF8) and prints it to stdout"""


def to_json_string(my_obj):
    """Function that returns the JSON
    representation of an object (string)"""
    import json
    return json.dumps(my_obj)
