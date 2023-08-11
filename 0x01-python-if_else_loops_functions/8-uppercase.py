#!/usr/bin/python3

def uppercase(str):
    lower_case = ''
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            lower_case += "{}".format(chr(ord(c) - 32))
        else:
            lower_case += c
    print('{}'.format(lower_case))
