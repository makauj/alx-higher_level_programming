#!/usr/bin/python3
import sys

if __name__ == "__main__":

    argc = len(sys.argv) - 1

    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
    else:
        print("{} arguments:".format(argc))
    for i in range(argc):
        print("{}: {}".format(i + 1, sys.argv[1 + i]))
