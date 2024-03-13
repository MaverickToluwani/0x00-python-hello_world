#!/usr/bin/python3
num1 = 0
num2 = 0
for alp in range(1, 27):
    if alp % 2 == 1:
        lower_alp = ord('z') - num1
        print(chr(lower_alp), end="")
        num1 += 2
    elif alp % 2 == 0:
        upper_alp = ord('Y') - num2
        print(chr(upper_alp), end="")
        num2 += 2
