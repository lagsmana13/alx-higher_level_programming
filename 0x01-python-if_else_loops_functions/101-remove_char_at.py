#!/usr/bin/python3
def custom_remove_char_at(string, index):
    new_string = ""
    for i in range(len(string)):
        if i == index:
            continue
        else:
            new_string += string[i]
    return new_string
