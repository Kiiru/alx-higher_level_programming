#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in range(0, x):
        try:
            if j < x:
                print("{:d}".format(int(my_list[i])), end='')
                j = j + 1
            else:
                break
        except (TypeError, ValueError):
            pass
    print()
    return (j)
