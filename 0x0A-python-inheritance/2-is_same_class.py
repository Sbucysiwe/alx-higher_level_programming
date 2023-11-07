#!/usr/bin/python3
"""Establishes class-checking function."""


def is_same_class(obj, a_class):
    """Determine if object is exactly precise instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an  precise instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
