#!/usr/bin/python3
""" Response header value #0 """
import sys
import urllib.request


url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    header_id = response.getheader('X-Request-Id')

print(header_id)
