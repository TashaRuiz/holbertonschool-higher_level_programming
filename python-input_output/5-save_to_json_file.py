#!/usr/bin/python3
"""Module that reads a text file (UTF8) and prints it to stdout"""


def save_to_json_file(my_obj, filename):
    import json
    with open(filename,'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
