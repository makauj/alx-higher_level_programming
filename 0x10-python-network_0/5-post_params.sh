#!/bin/bash
# Take in a URL, send a POST request, and displays the body of the response
curl -sX POST -d "email=test@gmail.com&subject=I will always be there for PLD" "$1"
