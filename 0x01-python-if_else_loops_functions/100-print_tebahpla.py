#!/usr/bin/python3
num1 = 0
num2 = 0
for alp in range(1, 27):
    if alp % 2 == 1:
        alp = ord('z') - num1
        num1 += 2
    elif alp % 2 == 0:
        alp = ord('Y') - num2
        num2 += 2
    print("{}".format(chr(alp)), end="")
