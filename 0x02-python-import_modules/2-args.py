#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_count = len(argv) - 1

    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
        print("{}: {}".format(1, argv[1]))
    else:
        print("{} arguments:".format(arg_count))
        for i in range(1, arg_count + 1):
            print("{}: {}".format(i, argv[i]))
