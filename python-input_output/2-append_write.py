#!/usr/bin/python3
"""Module that reads a text file (UTF8) and prints it to stdout"""


def append_write(filename="", text=""):
    """Function that appends a string to the end of a text file (UTF8)
    and returns the number of characters written"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
