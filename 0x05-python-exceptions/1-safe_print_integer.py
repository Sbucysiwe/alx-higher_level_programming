&sp=CAASBggFEAEoAQ%253D%253D
&sp=EgQQASgB

#!/usr/bin/python3


def safe_print_integer(value):
    """Print an integer with "{:d}".format().
    Args:
        value (int): integer to print.
    Returns:
        TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
