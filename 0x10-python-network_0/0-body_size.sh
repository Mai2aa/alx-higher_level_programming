#!/bin/bash
#sends a request to the URL, and displays the size of the body
curl -sI "$1" | awk '/Content-Length/ {print $2}'
