#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if chr(a) != 'i' and chr(a) != 'x':
        print("{:c}".format(a), end='')
