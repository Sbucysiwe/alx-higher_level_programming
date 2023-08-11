#!/usr/bin/python3
# 102-magic_calculation.py


def magic_calculation(a, b, c):
"""Validate the bytecode as specified by Holberton School."""
if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
