#!/usr/bin/python3
for i in range(99):
    if i < 10:
        print("0{}".format(i), end=", ")
    else:
        print(i, end=", ")
print("{}\n".format(i + 1), end="")
