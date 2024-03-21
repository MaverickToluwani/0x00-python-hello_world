#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_cp = my_list[:]
    count = 0
    for ele in list_cp:
        if ele == search:
            list_cp[count] = replace
        count += 1
    return list_cp
