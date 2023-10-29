#!/usr/bin/python3
def safe_print_integer_err(value):
    """
    Prints an integer.

    :param value: Value to print.
    :return: True if value has been correctly printed, Otherwise, returns False
              and prints in stderr the error precede by Exception.
    """
    import sys
    try:
        print("{:d}".format(value))
        return (True)

    except (ValueError, TypeError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return (False)