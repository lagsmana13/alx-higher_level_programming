#!/usr/bin/python3

def max_integer(my_list=None):
    if my_list is None or len(my_list) == 0:
        return None

    largest = my_list[0]
    for element in my_list[1:]:
        if element > largest:
            largest = element
    return largest
