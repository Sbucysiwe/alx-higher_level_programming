#!/usr/bin/python3
"""Defines file-appending function."""


def append_write(filename="", text=""):
    """Appends string to end of UTF8 text file.

    Args:
        filename (str): name of file to append to.
        text (str): string to append to file.
    Returns:
        number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
