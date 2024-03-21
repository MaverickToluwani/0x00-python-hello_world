#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    for ele in my_list:
        if ele not in uniq_list:
            uniq_list.append(ele)

    ul_len = len(uniq_list)
    sum = 0
    for i in range(ul_len):
        sum = sum + uniq_list[i]
    return sum
