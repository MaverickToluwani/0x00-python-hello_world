#!/usr/bin/python3
def uppercase(str):
    store = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            placement_in_alphabet_chain = ord(i) - ord('a')
            upper_value = ord('A') + placement_in_alphabet_chain
            store += chr(upper_value)
        else:
            store += i
    print("{}".format(store), end="")
    print("")
