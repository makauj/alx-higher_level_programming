#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)


    try:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
    except ValueError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {'+': add, '-': sub, '*': mul, '/': div}


    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    try:
        result = ops[operator](a, b)
        print(f"{a} {operator} {b} = {result}")

    except ZeroDivisionError:
        sys.exit(1)

if __name__ == "__main__":
    main()
