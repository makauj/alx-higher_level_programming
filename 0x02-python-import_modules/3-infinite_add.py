#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """"Retrieve command-line arguments"""
    args = sys.argv[1:]
    """Convert each argumnet to an int and compute sum"""
    total = sum(int(arg) for arg in args)
    """Print the result followed by a new line"""
    print(total)
