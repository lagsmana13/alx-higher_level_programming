#!/usr/bin/python3

def divisible_by_2(my_list=None):
    if my_list is None:
        return []

    new_l = []
    for element in my_list:
        if element % 2 == 0:
            new_l.append(1)
        else:
            new_l.append(0)
    return new_lxc
