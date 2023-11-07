#!/usr/bin/python3
"""Establish class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Determine if object is precise instance or inherited instance of class.

    Args:
        obj (any): The object to determine.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
