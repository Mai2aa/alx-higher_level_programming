#!/bin/bash
#sends a request to the URL, and displays the size of the body
url=$1
respose=$(curl -s -w "%{size_download}" -o /dev/null "$url")
echo "$response"
