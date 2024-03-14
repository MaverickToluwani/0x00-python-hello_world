#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    for arg in range(1, len(sys.argv)):
        sum = sum + int(sys.argv[arg])
    print(sum)
