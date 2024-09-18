#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(roman_string)):
        arabic = num[roman_string[i]]

        if i + 1 < len(roman_string) and arabic < num[roman_string[i + 1]]:
            total -= arabic
        else:
            total += arabic

    return total
