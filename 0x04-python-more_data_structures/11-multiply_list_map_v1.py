#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if my_list is not None and len(my_list) > 0:
        multiple_list = list(map(lambda x: x*number, my_list))
        return (multiple_list)
    else:
        return ([])
