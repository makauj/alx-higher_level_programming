#!/bin/bash
# Send a request to a URL, and display the rsponse status code
curl -s -o /dev/null -w "%(http_code)" "$1"
