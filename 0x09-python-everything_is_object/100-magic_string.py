#!/usr/bin/python3
def magic_string(n=[]):
    n[0] += 1
    return ("BestSchool" + ",BestSchool" * (n[0] - 1))
