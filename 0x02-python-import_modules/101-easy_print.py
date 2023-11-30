#!/usr/bin/python3

import os

def write_to_stdout(message):
    os.write(1, message.encode("UTF-8"))

if __name__ == "__main__":
    write_to_stdout("#pythoniscool\n")
