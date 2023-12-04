#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Changed to return a shallow copy of the original list
    new_list = my_list[:]  # Changed to create a shallow copy of the original list
    new_list[idx] = element
    return new_list
