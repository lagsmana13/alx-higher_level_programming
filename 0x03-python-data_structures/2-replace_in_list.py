#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()  # Changed to return a copy of the original list
    new_list = my_list.copy()  # Renamed variable for clarity
    new_list[idx] = element  # Changed to modify the copy instead of the original list
    return new_list
