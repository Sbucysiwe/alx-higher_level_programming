#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    """Display a series of numbers from 1 to 100, each separated by a space.

    Replace numbers divisible by three with Fizz.
    Replace numbers divisible by five with Buzz.
    Replace numbers divisible by both three and five with FizzBuzz.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
