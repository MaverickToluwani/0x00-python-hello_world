#!/usr/bin/python3
def max_integer(my_list=[]):
    lenlist = len(my_list)
    idxrange = lenlist - 1
    listcp = my_list[:]

    if lenlist == 0:
        return
    else:
        while idxrange > 0:
            j = 0
            while j < idxrange:
                if listcp[j] > listcp[j+1]:
                    temp = listcp[j]
                    listcp[j] = listcp[j+1]
                    listcp[j+1] = temp
                j += 1
            idxrange -= 1

    return listcp[lenlist-1]
