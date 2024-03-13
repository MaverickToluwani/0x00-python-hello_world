#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = (-1*number)%10
    last_digit = -1*last_digit
else:
    last_digit = number%10

if last_digit > 5:
    print("Last digit of {} is {} and is greater than {}\n".format(number, last_digit, 5))
elif last_digit == 0:
     print("Last digit of {} is {} and is {}\n".format(number, last_digit, 0))
elif last_digit < 6 and last_digit != 0:
     print("Last digit of {} is {} and is less than {} and not {}\n".format(number, last_digit, 6, 0))
