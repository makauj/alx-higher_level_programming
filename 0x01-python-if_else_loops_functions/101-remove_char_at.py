#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    c = 0
    for i in str:
        if c == n:
            pass
        else:
            result += c
        i += 1
    return result
