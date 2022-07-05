#!/usr/bin/python3
""""reads a file from a text"""


def read_file(filename=""):
    """Prints contents using utf coding format"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
