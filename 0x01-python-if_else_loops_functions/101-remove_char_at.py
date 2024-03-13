#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str):
        return str
    if n < 0:
        return str
    for i in range(len(str)):
        if str[i] == str[n]:
            continue
        else:
            print(str[i], end="")
    return ""
