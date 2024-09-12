#!/usr/bin/python3
import sys
from calculator_1 import add, sub, div, mul

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    op = sys.argv[2]

    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /\n")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = ops[op](a, b)
    print("{} {} {} = {}".format(a, op, b, result))
