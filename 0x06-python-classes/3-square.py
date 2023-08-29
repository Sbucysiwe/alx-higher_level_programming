#!/usr/bin/python3
"""State class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Start new square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return current area of square."""
        return (self.__size * self.__size)
