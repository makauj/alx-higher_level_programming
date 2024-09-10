#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 0 or n >= len(s):
        return None
    result = ""
    for index, char in enumerate(s):
        if index != n:
            result += char
    return result
