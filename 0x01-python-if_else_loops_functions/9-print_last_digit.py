#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastDigit = abs(number) % 10
        print(lastDigit, end="")
    else:
        lastDigit = number % 10
        print(lastDigit, end="")
    return lastDigit
