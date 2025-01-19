#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
import sys
from urllib import error, request


if __name__ == "__main__":
    url = sys.argv[1]

    request = request.Request(url)
    try:
        with request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as err:
        print(f"Error code: {err.code}")
