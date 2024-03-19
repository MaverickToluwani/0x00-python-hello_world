#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list[:]
    list_len = len(my_list)

    if idx < 0:
        return
    elif idx >= list_len:
        return

    list_copy[idx] = element
    return list_copy
