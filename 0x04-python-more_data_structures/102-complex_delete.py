#!/usr/bin/python3
def complex_delete(my_dict, value):
    keys_to_del = [key for key in my_dict if my_dict[key] == value]
    for key in keys_to_del:
        del my_dict[key]
    return my_dict
