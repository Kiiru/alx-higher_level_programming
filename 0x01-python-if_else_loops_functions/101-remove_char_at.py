#!/usr/bin/python3

def remove_char_at(str, n):
    j = 0
    copy = ''
    for i in str:
        if j != n:
            copy += i
        j += 1
    return copy
