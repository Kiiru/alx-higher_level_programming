#!/usr/bin/python3
def no_c(my_string):
    if len(my_string) > 0:
        i = 0
        idx_list = []
        for c in my_string:
            if c == 'c' or c == 'C':
                idx_list.append(i)
            i += 1

        i = 0
        dup_list = ''
        for r in range(0, len(my_string)):
            if i not in idx_list:
                dup_list += my_string[i]
            i += 1

        return dup_list

    return my_string
