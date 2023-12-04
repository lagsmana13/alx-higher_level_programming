#!/usr/bin/python3

def print_reversed_list_integer(my_list=None):
    if my_list is not None:  # Changed the condition to check for None explicitly
        for i in reversed(my_list):
            print("{:d}".format(i))
