#!/usr/bin/python3
def print_alternate_reverse():
    result = ""
    for i in range(26):
        if i % 2 == 0:
            result += chr(122 - i)
        else:
            result += chr(89 - (i - 1))
    print("{}".format(result), end="")
