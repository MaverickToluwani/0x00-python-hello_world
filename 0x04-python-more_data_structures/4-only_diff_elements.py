#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_ele = []
    if set_1 == []:
        return set_2
    if set_2 == []:
        return set_1
    for i in set_1:
        for j in set_2:
            if j not in set_1 and j not in diff_ele:
                diff_ele.append(j)
        if i not in set_2 and i not in diff_ele:
            diff_ele.append(i)

    return diff_ele
