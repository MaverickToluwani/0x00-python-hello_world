#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    if x == 0:
        return count
    try:
        for idx in range(x):
            if type(my_list[idx]) == int:
                print("{:d}".format(my_list[idx]), end="")
                count += 1
        print("")
    except IndexError as error:
        raise error
    return count
