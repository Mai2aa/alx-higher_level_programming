#!/usr/bin/python3
""" list 10 commits from the repository rails"""
import requests
import sys


if __name__ == "__main__":
    url = "https://developer.github.com/v3/repos/commits/".format(
            sys.argv[1], sys.argv[2])
    response = requests.get(url)
