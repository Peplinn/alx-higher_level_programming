#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Safely prints x elements of a list, if x > len(list), print until end

    :param my_list: List to print.
    :param x: Number of elements to print.
    :return: Number of the elements printed.
    """
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count += 1

    except IndexError:
        pass

    print()
    return (count)