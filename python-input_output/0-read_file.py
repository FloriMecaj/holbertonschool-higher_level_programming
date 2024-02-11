#!/usr/bin/python3
"""A func that reads files"""


def read_file(filename=""):
    """Read file"""
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
