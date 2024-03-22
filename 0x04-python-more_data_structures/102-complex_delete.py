#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = list(a_dictionary.keys())
    val_list = list(a_dictionary.values())
    count = 0
    for val in val_list:
        if val == value:
            del(a_dictionary[key_list[count]])
        count += 1
    return a_dictionary
