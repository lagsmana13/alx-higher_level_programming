#!/usr/bin/python3

def delete_at(my_list=None, idx=0):
    if my_list is None:
        return []

    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = my_list.copy()  # Create a copy of my_list
    del new_list[idx]
    return new_list
