#!/usr/bin/python3
for i in range(99):
    first_ = "0{}, ".format(i)
    next_ = "{}, ".format(i)
    print(first_ if i < 10 else next_, end="")
print("99\n", end="")
