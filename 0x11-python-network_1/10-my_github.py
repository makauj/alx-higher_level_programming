#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""
from requests import get
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    credentials = HTTPBasicAuth(sys.argv[1, sys.argv[2]])
    r = get("https://api.github.com/user", auth=credentials)
    print(r.json().get("id"))
