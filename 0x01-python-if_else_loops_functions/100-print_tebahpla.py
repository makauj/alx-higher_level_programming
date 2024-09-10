#!/usr/bin/python3
result = ""
for i in reversed(range(97, 123)):
    if i % 2 == 0:
        result += chr(i)
    else:
        result += chr(i - 32)
print("{}".format(result), end="")
