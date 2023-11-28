#!/usr/bin/python3
for i in range(1, 9):
    for j in range(i + 2, 12):
        print("{:02d}{:02d}".format(i, j), end=', ')
print("{:02d}{:02d}".format(i + 1, j))
