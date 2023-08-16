#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dup_dict = {}
    for k, v in a_dictionary.items():
        dup_dict[k] = a_dictionary.get(k) * 2
    return (dup_dict)
