#!/usr/bin/env bash
# Bash script that send a DELETE request to a URL passed as the first argument
# and displays the body of the response

curl -sX DELETE "$1"
