#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argL = len(sys.argv) - 1
    if argL == 0:
        print("{:d} arguments.".format(argL))
    if argL == 1:
        print("{:d} argument:".format(argL))
        print("{:d}: {:s}".format(argL, sys.argv[argL]))
    elif argL > 1:
        print("{:d} arguments:".format(argL))
        j = 1
        for i in range(0, argL):
            print("{:d}: {:s}".format(j, sys.argv[j]))
            j += 1
