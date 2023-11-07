#!/usr/bin/python3
"""Describes a function that is used to access object attributes."""


def lookup(obj):
    """Returns a list of object's available attributes."""
    return (dir(obj))
