#!/usr/bin/python3
"""Module that reads a text file (UTF8) and prints it to stdout"""


def from_json_string(my_str):
    """Function that returns an object (Python data structure)"""
    import json
    return json.loads(my_str)
