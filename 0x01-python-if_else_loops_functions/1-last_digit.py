#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number - (10 * int(number / 10))
str = "Last digit of"
if digit > 5:
    print("{} {} is {} and is greater than 5".format(str, number, digit))
elif digit == 0:
    print("{} {} is {} and is 0".format(str, number, digit))
elif digit < 6 and digit != 0:
    print("{} {} is {} and is less than 6 and not 0".format(str, number, digit))
