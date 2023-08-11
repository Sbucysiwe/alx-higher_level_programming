#!/usr/bin/python3
# 6-print_comb3.py

"""Generate all distinct pairs of ascending digits.

Ensure that the pairs consist of different digits; pairs like 01 and 10 are to be treated as the same.
"""

pairs = []

for digit1 in range(0, 9):  # Update the range to go up to 9 for digit1
    for digit2 in range(digit1 + 1, 10):
        pairs.append("{}{}".format(digit1, digit2))

print(", ".join(pairs))  # Join the list elements with commas and print
