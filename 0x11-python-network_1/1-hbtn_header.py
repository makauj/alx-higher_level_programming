#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""
from urllib import request
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    with request.urlopen(url) as value:
        print(dict(value.headers).get("X-Request-Id"))
