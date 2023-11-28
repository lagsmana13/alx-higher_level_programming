#!/usr/bin/python3
for num in range(122, 96, -1):
    if num % 2 == 0:
        letter = chr(num)
    else:
        letter = chr(num - 32)
    print(letter, end=" ")
