#!/usr/bin/env python3
custom_islower = __import__('7-islower').islower

print("a is {}".format("lower" if custom_islower("a") else "upper"))
print("H is {}".format("lower" if custom_islower("H") else "upper"))
print("A is {}".format("lower" if custom_islower("A") else "upper"))
print("3 is {}".format("lower" if custom_islower("3") else "upper"))
print("g is {}".format("lower" if custom_islower("g") else "upper"))
