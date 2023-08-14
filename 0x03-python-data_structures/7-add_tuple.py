#!/usr/bin/python3
def format_tuple(tuple_x=()):
    if len(tuple_x) == 0 or tuple_x is None:
        tuple_x = (0, 0)
        return tuple_x
    elif len(tuple_x) < 2:
        for i in range(len(tuple_x), 3):
            tuple_x = tuple_x + (0,)
        return tuple_x
    elif len(tuple_x) > 2:
        return tuple_x[0:2]
    return tuple_x


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = format_tuple(tuple_a)
    tuple_b = format_tuple(tuple_b)
    sum_tuple_a = tuple_a[0] + tuple_b[0]
    sum_tuple_b = tuple_a[1] + tuple_b[1]
    return sum_tuple_a, sum_tuple_b
