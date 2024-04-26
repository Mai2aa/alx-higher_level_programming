#!/usr/bin/python3
""" Response header value #1 """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    header_id = response.headers.get('X-Request-Id')
    print(header_id)
