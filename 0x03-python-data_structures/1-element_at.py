#!/usr/bin/python3
def element_at(my_list, idx):
    len_list = len(my_list)

    if idx < 0:
        return
    if idx >= len_list:
        return
    for ele in range(len_list):
        if idx == ele:
            return my_list[ele]
