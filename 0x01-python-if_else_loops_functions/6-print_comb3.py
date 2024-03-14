#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        if i >= 8:
            continue
        else:
            print("{}{}".format(i, j), end=", ")
print("{}{}".format(i-1, j))
