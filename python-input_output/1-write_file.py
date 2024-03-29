#!/usr/bin/python3
"""A func that writes files"""


def write_file(filename="", text=""):
    """Write file"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
