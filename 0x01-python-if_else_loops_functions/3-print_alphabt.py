#!/usr/bin/python3
for i in range(97, 123):
    if ord('q') != i and ord('e') != i:
        print("{:s}".format(chr(i)), end="")
