#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argL = len(sys.argv) - 1
    s = 0
    if argL == 0:
        print("{:d}".format(argL))
    else:
        for i in range(1, argL + 1):
            s += int(sys.argv[i])
        print("{:d}".format(s))
