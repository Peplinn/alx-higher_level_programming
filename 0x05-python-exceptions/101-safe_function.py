#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Executes a function safely.

    :param fct: Function pointer.
    :param args: Arguments to the function.
    :return: Result of the function, ELSE, None if
             something happens and prints in stderr the
             error preceded by Exception:
    """
    try:
        result = fct(*args)
        return (result)

    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return (None)