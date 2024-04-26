#!/usr/bin/python3
"""  Error code #0 """
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e))
