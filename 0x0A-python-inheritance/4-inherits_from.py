#!/usr/bin/python3
"""Establish an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Determine if object is an inherited instance of class.

    Args:
        obj (any): The object to Dertemine.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
