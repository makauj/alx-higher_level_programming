#!/bin/bash
# Take in a URL as an argument, send a GET request, and display the body
curl -sH "X-School-User-Id: 98" "$1"
