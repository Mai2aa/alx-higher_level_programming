#!/usr/bin/python3
""" Error code #1 using requests package"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    num_of_error = response.status_code
    if num_of_error >= 400:
        print("Error code: {}".format(num_of_error))
    else:
        content = response.text
        print(content)
