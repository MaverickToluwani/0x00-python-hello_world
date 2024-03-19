#!/usr/bin/python3
def no_c(my_string):
    editedStr = ""

    for ele in my_string:
        if ele.lower() == 'c':
            pass
        else:
            editedStr += ele
    return editedStr
