#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    val = {"email": argv[2]}
    data = parse.urlencode(val).encode("ascii")

    request = request.Request(url, data)
    with request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
