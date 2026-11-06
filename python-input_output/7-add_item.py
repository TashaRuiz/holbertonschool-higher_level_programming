#!/usr/bin/python3
"""Module that reads a text file (UTF8) and prints it to stdout"""
import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

"""Load the existing list if the file exists."""
try:
    items = load_from_json_file(filename)

except FileNotFoundError:
    items = []

"""Add the command-line arguments to the list."""
for arg in sys.argv[1:]:
    items.append(arg)

"""Save the updated list back to the file."""
save_to_json_file(items, filename)
