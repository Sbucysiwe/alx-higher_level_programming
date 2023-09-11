#!/usr/bin/python3
"""Defines function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add new attribute to object if possible.

    Args:
        obj (any): object to add attribute to.
        att (str): name of attribute to add to obj.
        value (any): value of att.
    Raises:
        TypeError: If attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
