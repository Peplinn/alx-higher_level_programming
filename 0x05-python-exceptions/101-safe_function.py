#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Executes a function safely.

    :param fct: Function pointer.
    :param args: Arguments to the function.
    :return: Returns the result of the function,Otherwise, returns None if
             something happens during the function and prints in stderr the
             error precede by Exception:
    """
    try:
        result = fct(*args)
        return (result)

    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return (None)