#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
isNeg = False
if number < 0:
    number *= -1
    isNeg = True

last_digit = number % 10
if isNeg:
    number *= -1
    last_digit *= -1

out = "Last digit of {} is {} {}"
if last_digit > 5:
    print(out.format(number, last_digit, 'and is greater than 5'))
elif last_digit == 0:
    print(out.format(number, last_digit, 'and is 0'))
elif last_digit < 6 and last_digit != 0:
    print(out.format(number, last_digit, 'and is less than 6 and not 0'))
else:
    pass
