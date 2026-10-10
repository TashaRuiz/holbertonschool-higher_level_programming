#!/usr/bin/python3
"""""
import hidden_4

if __name__ == "__main__":
    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)
            """""

"""
The program has been written to /tmp/4-hidden_discovery.py and 
hidden_4.pyc has been downloaded to /tmp/.Has been created the file in the holberton sandbox.

This solution:
Prints one name per line in alphabetical order.
Excludes names beginning with __.
Does not execute the discovery code when the script is imported, 
thanks to the if __name__ == "__main__": guard.
"""