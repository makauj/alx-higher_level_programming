#!/bin/bash
# Bash script that takes in a URL, sends a request to it and displays
# the size of the body of the respnse
curl -s "$1" | wc -c
