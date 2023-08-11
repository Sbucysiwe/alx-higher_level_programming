#!/usr/bin/python3
# 6-print_comb3.py

"""Generate all distinct pairs of ascending digits.

    Ensure that the pairs consist of different digits; pairs like 01 and 10 are to be treated as the same.
    """
for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}".format(digit1, digit2), end=", ")
