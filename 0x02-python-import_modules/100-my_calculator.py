#!/usr/bin/python3
import sys
from calculator_1 import add, sub, div, mul

if __name__ == "__main__":
    msg = "Unknown operator. Available operators: +, -, * and /"
    if len(sys.argv) < 4:
        sys.stderr.write(msg)

    def calculator():
        if len(sys.argv) < 4:
            sys.stderr.write(msg)
            return 1

        a = int(sys.argv[1])
        b = int(sys.argv[3])
        sign = sys.argv[2]
        if sign == "+":
            print("{} {} {} = {} ".format(a, sign, b, add(a, b)))
            return 0
        elif sign == "-":
            print("{} {} {} = {} ".format(a, sign, b, sub(a, b)))
            return 0
        elif sign == "*":
            print("{} {} {} = {} ".format(a, sign, b, mul(a, b)))
            return 0
        elif sign == "/":
            print("{} {} {} = {} ".format(a, sign, b, div(a, b)))
            return 0
        else:
            sys.stderr.write(msg)
            return 1

print(calculator())
