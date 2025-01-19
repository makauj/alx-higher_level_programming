#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
"""
import requests
import sys


if __name__ == "__maina__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    r = requests.get(url)
    commits = r.json()

    try:
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except IndexError:
        pass
