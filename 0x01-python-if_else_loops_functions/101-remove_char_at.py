#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return None
    new_string = str[:n] + str[n+1:]
    return new_string
