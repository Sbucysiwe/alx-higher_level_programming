#!/usr/bin/python3
"""Establishes an inherited list class MyList."""


class MyList(list):
    """Enables sorted printing functionality for the native list class."""

    def print_sorted(self):
        """Prints list in sorted ascending order."""
        print(sorted(self))
