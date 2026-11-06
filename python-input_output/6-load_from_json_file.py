#!/usr/bin/python3
"""Module that reads a text file (UTF8) and prints it to stdout"""
import json


def load_from_json_file(filename):
    """Create and return an object from a JSON file."""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
