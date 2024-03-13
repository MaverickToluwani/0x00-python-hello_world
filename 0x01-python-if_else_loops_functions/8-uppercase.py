#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            placement_in_alphabet_chain = ord(i) - ord('a')
            upper_value = ord('A') + placement_in_alphabet_chain
            print("{}".format(chr(upper_value)), end="")
        else:
            print("{}".format(i), end="")
    print("\n")
