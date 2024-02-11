#!/usr/bin/python3
"""A func that appends files"""


def append_write(filename="", text=""):
    """append file"""
    with open(filename, 'a', encoding="utf-8") as f:
        content = f.write(text)
    return len(text)
