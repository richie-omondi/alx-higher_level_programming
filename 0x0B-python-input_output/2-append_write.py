#!/usr/bin/python3
""" Module that contains a function that appends a string to a text file
"""


def append_write(filename="", text=""):
    """ Function that appends a string to a text file

    Args:
        filename: filename
        text: text to write

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
