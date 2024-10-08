#!/usr/bin/python3
"""function that prints a text with 2 new lines after
each of these characters: `.`, `?` and `:`
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    length = len(text)

    while i < length and text[i] == " ":
        i = i + 1

    while i < length:
        print(text[i], end="")
        if text[i] in ".?:" or text[i] == "\n":
            if text[i] in ".?:":
                print("\n")

            i = i + 1

            """Skip any spaces that follow the punctuation"""
            while i + 1 < length and text[i] == ' ':
                i = i + 1
            continue

        i = i + 1
